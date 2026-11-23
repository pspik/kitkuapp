"""Buduje stronę z CHANGELOG.md: zmiany/index.html (cała historia) i sekcję „Co nowego” w index.html.
Uruchom po każdej zmianie aplikacji: python3 tools/build.py"""
import html, re, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
md = (root / "CHANGELOG.md").read_text(encoding="utf-8")
vers = []  # (nagłówek, [punkty])
for line in md.splitlines():
    if line.startswith("## "): vers.append((line[3:].strip(), []))
    elif line.startswith("- ") and vers: vers[-1][1].append(line[2:].strip())
def block(h, items):
    v, _, d = h.partition(" — ")
    lis = "".join(f"<li>{html.escape(i)}</li>" for i in items)
    return f'<section class="ver"><h2>{html.escape(v)} <span>{html.escape(d)}</span></h2><ul>{lis}</ul></section>'
STYLE = """:root{color-scheme:light dark;--bg:light-dark(#ffffff,#0F1520);--ink:light-dark(#16201c,#e7eeeb);--mut:light-dark(#56606a,#a3adbb);--acc:light-dark(#0B5A64,#E0AFC0);--line:light-dark(#dfe3ea,#263042)}
*{box-sizing:border-box;min-width:0}body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.6 Inter,system-ui,sans-serif}
main{max-width:760px;margin:0 auto;padding:clamp(28px,5vw,56px) max(5vw,18px) 64px}a{color:var(--acc)}
h1{font-size:clamp(30px,5vw,40px);line-height:1.1;margin:8px 0 18px}.ver{border-top:1px solid var(--line);padding:14px 0 4px}
.ver h2{font-size:20px;margin:0 0 4px}.ver h2 span{font-size:15px;font-weight:400;color:var(--mut);margin-left:8px}ul{padding-left:22px;margin:6px 0}li{margin:4px 0}"""
page = f"""<!DOCTYPE html>
<html lang="pl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>KitkuApp – historia zmian</title><link rel="icon" href="../ikona.png">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<style>{STYLE}</style></head><body><main>
<p><a href="../">← KitkuApp</a></p><h1>Historia zmian</h1>
{"".join(block(h, i) for h, i in vers)}
</main></body></html>
"""
(root / "zmiany" / "index.html").write_text(page, encoding="utf-8")
# „Co nowego” na stronie głównej: najnowsza wersja
idx = root / "index.html"
s = idx.read_text(encoding="utf-8")
new = f'<!--NOWE-->{block(*vers[0])}<p><a href="zmiany/">Pełna historia zmian</a></p><!--/NOWE-->'
s = re.sub(r"<!--NOWE-->.*?<!--/NOWE-->", lambda m: new, s, flags=re.S)
idx.write_text(s, encoding="utf-8")
print("wersji:", len(vers), "najnowsza:", vers[0][0])
