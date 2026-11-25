import subprocess, sys

XF = 0.6  # crossfade length between sections
EDGE = 0.5  # fade from/to black at start/end so the loop restarts cleanly


def build(src, segs, out, crf=25):
    inputs, chains = [], []
    for i, (start, dur) in enumerate(segs):
        inputs += ["-ss", str(start), "-t", str(dur), "-i", src]
        chains.append(f"[{i}:v]scale=1440:900:flags=lanczos,fps=30,format=yuv420p,setpts=PTS-STARTPTS[v{i}]")
    prev, offset = "v0", 0.0
    for i in range(1, len(segs)):
        offset += segs[i - 1][1] - XF
        chains.append(f"[{prev}][v{i}]xfade=transition=fade:duration={XF}:offset={offset:.3f}[x{i}]")
        prev = f"x{i}"
    total = sum(d for _, d in segs) - XF * (len(segs) - 1)
    chains.append(f"[{prev}]fade=t=in:st=0:d={EDGE},fade=t=out:st={total - EDGE:.3f}:d={EDGE}[out]")
    cmd = ["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(chains), "-map", "[out]", "-an",
           "-c:v", "libx264", "-preset", "slow", "-crf", str(crf), "-profile:v", "high", "-pix_fmt", "yuv420p",
           "-movflags", "+faststart", out]
    subprocess.run(cmd, check=True)
    print(out, f"{total:.1f}s")


if __name__ == "__main__":
    build("/home/claude/demos/sp.mp4",
          [(87, 5), (40, 4.5), (133, 4.5), (121, 4.5), (201, 4.5), (240, 4.5)],
          "/home/claude/demos/sp_highlight.mp4")
    build("/home/claude/demos/aiml.mp4",
          [(4, 3.5), (11, 4.5), (23, 4.5), (28, 4.5), (47, 4.5)],
          "/home/claude/demos/aiml_highlight.mp4")
