import asyncio, pathlib
ROOT = pathlib.Path(__file__).parent
OUT = {"clay": "Miguel-Freitas-CV-SoftClay.pdf", "tide": "Miguel-Freitas-CV-Tide.pdf"}
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for name in OUT:
            pg = await b.new_page()
            await pg.goto((ROOT / f"{name}.html").as_uri())
            await pg.evaluate("document.fonts.ready")
            await pg.wait_for_timeout(400)
            await pg.pdf(path=str(ROOT.parent.parent / "assets/cv" / OUT[name]), prefer_css_page_size=True, print_background=True)
        await b.close()
asyncio.run(main())
