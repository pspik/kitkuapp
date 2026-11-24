import json, html, os
HERE = os.path.dirname(os.path.abspath(__file__))
meta = json.load(open(os.path.join(HERE, 'meta.json')))
css = """
:root{color-scheme:light dark;--bg:light-dark(#ffffff,#0F1520);--ink:light-dark(#16201c,#e7eeeb);--mut:light-dark(#56606a,#a3adbb);--acc:light-dark(#0B5A64,#E0AFC0);--line:light-dark(#dfe3ea,#263042);--card:light-dark(#F4F6F8,#172133)}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.6 Inter,system-ui,sans-serif}
header{background:linear-gradient(135deg,#0B5A64,#123A52 55%,#172040);color:#fff;padding:clamp(28px,6vw,56px) max(6vw,20px)}
.in{max-width:980px;margin:0 auto}.top{display:flex;align-items:center;gap:14px}.top img{width:52px;height:52px;border-radius:50%;box-shadow:0 4px 14px rgba(0,0,0,.25)}
h1{font-size:clamp(30px,6vw,46px);line-height:1.1;margin:0}.lead{color:#F1D3DC;margin:14px 0 0;max-width:46ch}
header a{color:#fff}
main{max-width:980px;margin:0 auto;padding:28px max(6vw,20px) 64px}
a{color:var(--acc)}.mut{color:var(--mut);font-size:15px}
nav.toc{display:flex;flex-wrap:wrap;gap:8px;margin:6px 0 10px}nav.toc a{text-decoration:none;border:1px solid var(--line);border-radius:999px;padding:5px 12px;font-size:15px}
section.scr{border-top:1px solid var(--line);padding:26px 0 8px;display:grid;grid-template-columns:300px 1fr;gap:28px;align-items:start}
section.scr h2{font-size:26px;margin:0 0 6px}
.shot{position:relative;width:300px;border-radius:26px;overflow:hidden;box-shadow:0 10px 28px rgba(0,0,0,.22);border:6px solid #1b1f24;position:sticky;top:12px}
.shot img{display:block;width:100%;height:auto}
.tap{position:absolute;width:26px;height:26px;margin:-13px 0 0 -13px;opacity:.95;border-radius:50%;background:#D9A3B6;color:#172040;font:700 14px/26px Inter,sans-serif;text-align:center;box-shadow:0 0 0 2px #fff,0 2px 8px rgba(0,0,0,.35);cursor:pointer;z-index:2}
.tap::after{content:"";position:absolute;inset:-2px;border-radius:50%;border:3px solid #D9A3B6;opacity:0;animation:ripple var(--cycle) ease-out infinite;animation-delay:var(--d)}
.tap.hot{background:#0B5A64;color:#fff}.tap.hot::after{border-color:#0B5A64}
@keyframes ripple{0%{transform:scale(1);opacity:.95}var(--x){}12%{transform:scale(2.6);opacity:0}100%{opacity:0}}
ol.steps{list-style:none;padding:0;margin:14px 0 0}ol.steps li{display:flex;gap:12px;padding:10px 12px;border-radius:14px;margin:4px 0;cursor:default;transition:background .15s}
ol.steps li.hot{background:var(--card)}
ol.steps .n{flex:none;width:28px;height:28px;border-radius:50%;background:#D9A3B6;color:#172040;font-weight:700;text-align:center;line-height:28px;font-size:14px;margin-top:1px}
ol.steps li.hot .n{background:#0B5A64;color:#fff}
.play{display:inline-flex;align-items:center;gap:6px;margin-top:6px;font-size:15px;border:1px solid var(--line);background:none;color:var(--acc);border-radius:999px;padding:5px 12px;cursor:pointer}
@media (max-width:720px){section.scr{grid-template-columns:1fr}.shot{position:relative;top:0;margin:0 auto;width:min(300px,86vw)}}
@media (prefers-reduced-motion:reduce){.tap::after{animation:none}}
footer{border-top:1px solid var(--line);margin-top:30px;padding-top:14px}
"""
css = css.replace("var(--x){}", "")
secs, toc = [], []
for m in meta:
    n = len(m['steps']); cycle = max(6, n * 1.6)
    taps = "".join(
        f'<span class="tap" data-n="{k}" style="left:{m["taps"][str(k)][0]}%;top:{m["taps"][str(k)][1]}%;--d:{(k-1)*1.6:.1f}s" aria-hidden="true">{k}</span>'
        for k, _ in m['steps'] if str(k) in m['taps'])
    steps = "".join(f'<li data-n="{k}"><span class="n">{k}</span><span>{txt}</span></li>' for k, txt in m['steps'])
    secs.append(f'''<section class="scr" id="{m["slug"]}" style="--cycle:{cycle:.1f}s">
<div class="shot"><img src="img/{m["slug"]}.jpg" alt="Ekran {html.escape(m["title"])} z przykładowymi danymi" width="780" height="{m["h"]*2}" loading="lazy">{taps}</div>
<div><h2>{m["title"]}</h2><p>{m["intro"]}</p><ol class="steps">{steps}</ol></div></section>''')
    toc.append(f'<a href="#{m["slug"]}">{m["title"]}</a>')
js = """
document.querySelectorAll('section.scr').forEach(sec=>{
  const taps=[...sec.querySelectorAll('.tap')], items=[...sec.querySelectorAll('ol.steps li')];
  const hot=n=>{taps.forEach(t=>t.classList.toggle('hot',t.dataset.n==n));items.forEach(i=>i.classList.toggle('hot',i.dataset.n==n));};
  items.forEach(i=>{i.addEventListener('mouseenter',()=>hot(i.dataset.n));i.addEventListener('mouseleave',()=>hot(null));i.addEventListener('click',()=>hot(i.dataset.n));});
  taps.forEach(t=>t.addEventListener('click',()=>{hot(t.dataset.n);const li=items.find(i=>i.dataset.n==t.dataset.n);if(li&&innerWidth<720)li.scrollIntoView({behavior:'smooth',block:'center'});}));
});
"""
page = f'''<!DOCTYPE html>
<html lang="pl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Podręcznik użytkownika – KitkuApp</title>
<meta name="description" content="Jak korzystać z KitkuApp: pulpit, profil zwierzaka, historia, import wyników, kalendarz, leki i zapasy, wykresy, przypomnienia, kopia zapasowa.">
<link rel="icon" href="../ikona.png">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<style>{css}</style></head><body>
<header><div class="in"><div class="top"><a href="../"><img src="../ikona.png" alt="KitkuApp – strona główna" width="52" height="52"></a><h1>Podręcznik użytkownika</h1></div>
<p class="lead">Co można zrobić na każdym ekranie KitkuApp. Zrzuty przedstawiają uproszczony wygląd aplikacji – mają zobrazować jej możliwości, więc szczegóły na telefonie mogą wyglądać nieco inaczej. Numery na zrzutach pokazują, gdzie dotknąć.</p></div></header>
<main>
<p class="mut">Zrzuty przedstawiają aplikację z przykładowymi, wymyślonymi danymi (Mruczek, Pestka, Luna). Dotknij numeru na zrzucie albo punktu w opisie, aby je powiązać,.</p>
<nav class="toc">{"".join(toc)}</nav>
{"".join(secs)}
<footer><p><a href="../">Strona główna</a> · <a href="../zmiany/">Lista zmian</a> · <a href="../polityka-prywatnosci/">Polityka prywatności</a></p></footer>
</main><script>{js}</script></body></html>'''
open(os.path.join(HERE, '../../podrecznik/index.html'), 'w').write(page)
print(len(page))
