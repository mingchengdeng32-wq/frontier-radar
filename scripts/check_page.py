"""发布前检查：截桌面首屏 + 检查 390px 宽度是否横向溢出。

用法: python3 scripts/check_page.py path/to/page.html [out_dir]
需要: pip install playwright && playwright install chromium（已有 Chromium 的环境可跳过安装）
"""
import os
import sys
from playwright.sync_api import sync_playwright

page_path = os.path.abspath(sys.argv[1])
out_dir = sys.argv[2] if len(sys.argv) > 2 else "."
os.makedirs(out_dir, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch()
    desk = browser.new_page(viewport={"width": 1280, "height": 1500})
    desk.goto("file://" + page_path)
    desk.wait_for_timeout(800)
    desk.screenshot(path=os.path.join(out_dir, "desktop.png"))

    mobile = browser.new_page(viewport={"width": 390, "height": 844})
    mobile.goto("file://" + page_path)
    mobile.wait_for_timeout(500)
    width = mobile.evaluate("document.documentElement.scrollWidth")
    mobile.screenshot(path=os.path.join(out_dir, "mobile.png"))
    browser.close()

ok = width <= 390
print(f"mobile scrollWidth={width} -> {'OK' if ok else 'OVERFLOW'}")
sys.exit(0 if ok else 1)
