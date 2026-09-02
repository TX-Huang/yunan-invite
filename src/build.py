# -*- coding: utf-8 -*-
"""把去背照片嵌進 invite-picker.html，產生可直接上線的 ../index.html。

照片層和破框的手用同一張圖、同一組位置，所以永遠對得準、不會有接縫。
"""
import base64, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)
SRC_HTML = os.path.join(HERE, "invite-picker.html")
CUTOUT = os.path.join(HERE, "cutout.webp")
OUT_SITE = os.path.join(SITE, "index.html")          # GitHub Pages 讀這個
OUT_LOCAL = os.path.join(HERE, "invite-cards.html")  # 本機預覽用

b64 = base64.b64encode(open(CUTOUT, "rb").read()).decode("ascii")
uri = "data:image/webp;base64," + b64
print("照片嵌入", len(b64) // 1024, "KB")

html = open(SRC_HTML, encoding="utf-8").read()

pat = re.compile(r"var PHOTO=.*?;\n", re.S)
assert pat.search(html), "找不到 PHOTO 這一行"
html = pat.sub("var PHOTO='" + uri + "';\n", html, count=1)

pat = re.compile(r"var ARM=.*?;\n", re.S)
assert pat.search(html), "找不到 ARM 這一行"
html = pat.sub("var ARM=PHOTO;\n", html, count=1)

for path in (OUT_SITE, OUT_LOCAL):
    open(path, "w", encoding="utf-8").write(html)
    print("寫出", os.path.relpath(path, SITE), len(html) // 1024, "KB")
