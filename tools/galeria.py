"""Galeria na stronie głównej z prawdziwych zrzutów telefonu (dane fikcyjne z kopii demo).
Zrzuty 1080×2340 w tools/galeria-src/ (nie trafiają do repo – .gitignore), nazwy jak w P poniżej.
    python3 tools/galeria.py   # → img/NN_slug.jpg (540×960), img/NN_slug-duzy.jpg (1080×1920) + galeria w index.html"""
import os, re, base64
from PIL import Image
from playwright.sync_api import sync_playwright
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SRC = os.path.join(ROOT, 'tools/galeria-src'); OUT = os.path.join(ROOT, 'img')
# panel: (slug, tytuł, podtytuł, alt, [fragmenty]); fragment: (plik, y0, y1, [(x0, y0, x1, y1, etykieta)])
# jeden fragment = ekran w ramce telefonu, dwa = karty jedna pod drugą
P = [
    ('pulpit', 'Zdrowie całego stada<br>na jednym ekranie', 'Najpierw zwierzaki, które wymagają uwagi', 'Pulpit',
     [('pulpit.jpg', 100, 2200, [(45, 1195, 1035, 1705, 'zaległe badanie')])]),
    ('zwierzaki', 'Wszystkie<br>zwierzaki', 'Kolejność od najpilniejszych badań', 'Lista zwierzaków',
     [('zwierzaki.jpg', 100, 2200, [(80, 635, 380, 730, '')])]),
    ('profil', 'Stan zdrowia<br>i terminy badań', 'Podsumowanie z ostatnich wyników', 'Profil – stan zdrowia i terminy',
     [('profil-stan.jpg', 860, 1665, []), ('profil-terminy.jpg', 130, 1220, [(815, 285, 1005, 380, '')])]),
    ('opieka', 'Dieta, fizjoterapia<br>i notatki', 'Cała opieka w profilu zwierzaka', 'Profil – dieta, fizjoterapia i notatki',
     [('profil-dieta.jpg', 100, 1060, []), ('profil-dieta.jpg', 1370, 1805, [])]),
    ('wykresy', 'Wyniki<br>na wykresach', 'Strzałki ‹ › zmieniają parametr, lista ma wyszukiwarkę', 'Wykresy wyników',
     [('wykresy.jpg', 140, 1040, [(80, 180, 1000, 320, '')]), ('wykresy-arkusz.jpg', 0, 1020, [(700, 765, 975, 850, '')])]),
    ('leki', 'Leki<br>i ich zapasy', 'Według godzin, z ostrzeżeniem o końcu zapasu', 'Leki i zapasy',
     [('leki.jpg', 580, 1460, []), ('zapasy.jpg', 130, 1050, [(870, 255, 1005, 350, '')])]),
    ('kalendarz', 'Wszystko<br>w kalendarzu', 'Wizyty, badania i terminy', 'Kalendarz',
     [('kalendarz.jpg', 100, 2200, [(745, 1125, 870, 1250, 'kolor = zwierzak')])]),
    ('import', 'Wyniki<br>bez przepisywania', 'Import z PDF, skanów i zdjęć', 'Import wyników',
     [('import.jpg', 100, 2200, [(40, 580, 1040, 700, '')])]),
    ('dane', 'Twoje dane<br>w Twoim telefonie', 'Kopia zapasowa i ciemny motyw', 'Kopia zapasowa i wygląd',
     [('dane-kopia.jpg', 130, 1420, []), ('dane-wyglad.jpg', 1450, 1905, [])]),
]
PAW = 'M12 13c-2.8 0-5 2.4-5 4.4 0 1.5 1.2 2.1 2.6 2.1 1 0 1.6-.4 2.4-.4s1.4.4 2.4.4c1.4 0 2.6-.6 2.6-2.1 0-2-2.2-4.4-5-4.4zM6.5 12.5a2 2.4 0 1 0 0-.01zM9.5 8.5a2 2.6 0 1 0 0-.01zM14.5 8.5a2 2.6 0 1 0 0-.01zM17.5 12.5a2 2.4 0 1 0 0-.01z'
PAWS = ''.join(f'<svg style="position:absolute;left:{x}px;top:{y}px;width:{s}px;transform:rotate({r}deg);opacity:.08" viewBox="0 0 24 24"><path fill="#fff" d="{PAW}"/></svg>'
               for x, y, r, s in [(30, 60, -20, 46), (470, 40, 25, 40), (470, 380, -15, 56), (10, 520, 18, 50), (480, 720, -30, 44), (30, 880, 12, 52)])
def crop(f, y0, y1):
    p = f'/tmp/galeria-{f}-{y0}-{y1}.jpg'
    Image.open(os.path.join(SRC, f)).convert('RGB').crop((0, y0, 1080, y1)).save(p, quality=92)
    return base64.b64encode(open(p, 'rb').read()).decode()
def marks(hl, y0, k):
    out = ''
    for x0, a, x1, b, lab in hl:
        st = f'left:{x0*k-5}px;top:{(a-y0)*k-5}px;width:{(x1-x0)*k+10}px;height:{(b-a)*k+10}px'
        out += f'<div class="hl" style="{st}">' + (f'<span>{lab}</span>' if lab else '') + '</div>'
    return out
def body(frags):
    if len(frags) == 1:
        f, y0, y1, hl = frags[0]; w = 360; k = w / 1080; h = (y1 - y0) * k
        return (f'<div class="ph" style="height:{h+20}px"><div class="sc" style="height:{h}px">'
                f'<img src="data:image/jpeg;base64,{crop(f, y0, y1)}" style="width:{w}px">{marks(hl, y0, k)}</div></div>')
    gap = 16; avail = 960 - 205 - 24 - gap
    tot = sum(y1 - y0 for _, y0, y1, _ in frags)
    w = min(460, avail / tot * 1080); k = w / 1080; out = ''; top = 205
    for f, y0, y1, hl in frags:
        h = (y1 - y0) * k
        out += (f'<div class="fr" style="top:{top}px;left:{(540-w)/2}px;width:{w}px;height:{h}px">'
                f'<img src="data:image/jpeg;base64,{crop(f, y0, y1)}" style="width:{w}px">{marks(hl, y0, k)}</div>')
        top += h + gap
    return out
def html(title, sub, frags):
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
html,body{{margin:0}}.c{{width:540px;height:960px;position:relative;overflow:hidden;font-family:Inter,'DejaVu Sans',Arial,sans-serif;
background:radial-gradient(ellipse at 15% 0%,rgba(20,120,130,.55),transparent 60%),radial-gradient(ellipse at 100% 100%,rgba(194,123,152,.35),transparent 55%),linear-gradient(135deg,#0B5A64,#123A52 55%,#172040)}}
h1{{position:absolute;top:44px;left:0;right:0;text-align:center;margin:0;color:#fff;font-size:38px;line-height:1.15;font-weight:700;letter-spacing:-.5px}}
p{{position:absolute;top:144px;left:24px;right:24px;text-align:center;margin:0;color:#E8C1CE;font-size:19px}}
.ph{{position:absolute;left:80px;top:205px;width:360px;background:#0C1220;border-radius:44px;padding:10px;box-shadow:0 24px 60px rgba(0,0,0,.45),inset 0 0 0 2px rgba(255,255,255,.12)}}
.sc{{position:relative;border-radius:34px;overflow:hidden}}.sc img,.fr img{{display:block}}
.fr{{position:absolute;border-radius:22px;overflow:hidden;box-shadow:0 18px 44px rgba(0,0,0,.45),0 0 0 2px rgba(255,255,255,.14)}}
.hl{{position:absolute;border:3px solid #E0AFC0;border-radius:16px;box-shadow:0 0 0 4px rgba(224,175,192,.35)}}
.hl span{{position:absolute;right:-6px;top:-30px;background:#E0AFC0;color:#172040;font-size:14px;font-weight:700;padding:4px 10px;border-radius:999px;white-space:nowrap}}
</style></head><body><div class="c">{PAWS}<h1>{title}</h1><p>{sub}</p>{body(frags)}</div></body></html>'''
for f in os.listdir(OUT):
    if re.match(r'\d+_.*\.jpg$', f): os.remove(os.path.join(OUT, f))
cells = []
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
    pg = b.new_page(viewport={'width': 540, 'height': 960}, device_scale_factor=2)
    for i, (slug, title, sub, alt, frags) in enumerate(P, 1):
        pg.set_content(html(title, sub, frags)); pg.wait_for_timeout(200)
        n = f'{i:02d}_{slug}'
        pg.screenshot(path=f'{OUT}/{n}-duzy.jpg', type='jpeg', quality=86)
        Image.open(f'{OUT}/{n}-duzy.jpg').resize((540, 960), Image.LANCZOS).save(f'{OUT}/{n}.jpg', quality=86)
        cells.append(f'<a href="img/{n}-duzy.jpg"><img src="img/{n}.jpg" alt="{alt}" loading="lazy" width="540" height="960"></a>')
    b.close()
p = os.path.join(ROOT, 'index.html'); s = open(p).read()
s = re.sub(r'<div class="shots">.*?</div>', '<div class="shots">' + ''.join(cells) + '</div>', s, count=1, flags=re.S)
open(p, 'w').write(s)
print(len(cells), 'paneli')
