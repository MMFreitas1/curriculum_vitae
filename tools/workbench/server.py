#!/usr/bin/env python3
"""Local CV text workbench. Run: python3 tools/workbench/server.py [port]"""
import json
import sys
from datetime import datetime, timezone
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
STAGING = HERE / "staging.json"


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def read_staging():
    try:
        return json.loads(STAGING.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return None


class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def send_json(self, code, obj):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path in ("/", ""):
            self.send_response(302)
            self.send_header("Location", "/tools/workbench/")
            self.end_headers()
            return
        if self.path.startswith("/api/status"):
            self.send_json(200, read_staging() or {"status": "empty"})
            return
        super().do_GET()

    def do_POST(self):
        if self.path != "/api/stage":
            self.send_json(404, {"error": "not found"})
            return
        try:
            length = int(self.headers.get("Content-Length", 0))
            data = json.loads(self.rfile.read(length).decode("utf-8"))
            edits = data.get("edits", [])
            note = str(data.get("note", "")).strip()
            if not isinstance(edits, list) or not all(
                isinstance(e, dict) and isinstance(e.get("key"), str) and isinstance(e.get("pt_after"), str)
                for e in edits
            ):
                raise ValueError("edits must be a list of {key, pt_after, ...}")
            if not edits and not note:
                raise ValueError("nothing to stage")
        except (ValueError, json.JSONDecodeError) as exc:
            self.send_json(400, {"error": str(exc)})
            return

        current = read_staging()
        if current and current.get("status") == "pending":
            merged = {e["key"]: e for e in current.get("edits", [])}
            for e in edits:
                if e["key"] in merged:
                    e["pt_before"] = merged[e["key"]].get("pt_before", e.get("pt_before"))
                merged[e["key"]] = e
            edits = list(merged.values())
            note = "\n\n".join(n for n in (current.get("note", ""), note) if n)
            job_id = current["id"]
        else:
            job_id = now()

        job = {"id": job_id, "status": "pending", "saved_at": now(), "note": note, "edits": edits}
        tmp = STAGING.with_suffix(".tmp")
        tmp.write_text(json.dumps(job, ensure_ascii=False, indent=2), encoding="utf-8")
        tmp.replace(STAGING)
        self.send_json(200, job)

    def log_message(self, fmt, *args):
        if "/api/status" not in (args[0] if args else ""):
            super().log_message(fmt, *args)


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    server = ThreadingHTTPServer(("127.0.0.1", port), partial(Handler, directory=str(ROOT)))
    print(f"Workbench: http://127.0.0.1:{port}/   (CV preview: http://127.0.0.1:{port}/index.html)", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
