"""Zrzuty do galerii na stronie głównej: makiety z podręcznika (fikcyjne dane) w ramce telefonu
na tle w barwach strony. Najpierw uruchom podrecznik/render.py.
    python3 tools/galeria.py   # → img/NN_slug.jpg (540×960) i img/NN_slug-duzy.jpg (1080×1920) + galeria w index.html"""
import os, re, base64
from PIL import Image
from playwright.sync_api import sync_playwright
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SRC = os.path.join(ROOT, 'podrecznik/img'); OUT = os.path.join(ROOT, 'img')
# (plik wyjściowy, makieta, przesunięcie: 'top' | 'bottom', tytuł, podtytuł, alt)
G = [
    ('pulpit', 'pulpit', 'top', 'Zdrowie całego stada<br>na jednym ekranie', 'Najpierw zwierzaki, które wymagają uwagi', 'Pulpit'),
    ('stan-zdrowia', 'profil', 'top', 'Stan zdrowia<br>w skrócie', 'Podsumowanie wyników, dieta, fizjoterapia, notatki', 'Profil zwierzaka – stan zdrowia'),
    ('terminy', 'profil', 'bottom', 'Terminy badań<br>każdego zwierzaka', 'Od zaległych do najodleglejszych', 'Profil zwierzaka – terminy badań'),
    ('historia', 'historia', 'top', 'Cała historia<br>pod ręką', 'Z wyszukiwarką i podziałem na lata', 'Historia zwierzaka'),
    ('import', 'import', 'top', 'Wyniki<br>bez przepisywania', 'Import z PDF, skanów i zdjęć', 'Import wyników'),
    ('wpis', 'wpis', 'top', 'Wyniki z normami<br>i zaleceniami', 'Pełny opis wizyty lub badania', 'Szczegóły wpisu'),
    ('wykresy', 'wykresy', 'top', 'Wyniki<br>na wykresach', 'Zmiany w czasie na tle normy', 'Wykresy wyników'),
    ('leki', 'leki', 'top', 'Leki według<br>godziny podawania', 'Z zapasami i historią leczenia', 'Leki'),
    ('kalendarz', 'kalendarz', 'top', 'Wszystko<br>w kalendarzu', 'Wizyty, badania i zaplanowane terminy', 'Kalendarz'),
    ('przypomnienia', 'przypomnienia', 'top', 'Przypomnienia<br>na czas', 'Częstotliwość badań do ustawienia', 'Przypomnienia'),
    ('dane', 'dane', 'top', 'Twoje dane<br>w Twoim telefonie', 'Kopia zapasowa i ciemny motyw', 'Kopia zapasowa i ustawienia'),
]
PAW = 'M12 13c-2.8 0-5 2.4-5 4.4 0 1.5 1.2 2.1 2.6 2.1 1 0 1.6-.4 2.4-.4s1.4.4 2.4.4c1.4 0 2.6-.6 2.6-2.1 0-2-2.2-4.4-5-4.4zM6.5 12.5a2 2.4 0 1 0 0-.01zM9.5 8.5a2 2.6 0 1 0 0-.01zM14.5 8.5a2 2.6 0 1 0 0-.01zM17.5 12.5a2 2.4 0 1 0 0-.01z'
def paws():
    pos = [(30, 60, -20, 46), (470, 40, 25, 40), (440, 360, -15, 56), (20, 520, 18, 50), (480, 700, -30, 44), (60, 860, 12, 52)]
    return ''.join(f'<svg style="position:absolute;left:{x}px;top:{y}px;width:{s}px;transform:rotate({r}deg);opacity:.08" viewBox="0 0 24 24"><path fill="#fff" d="{PAW}"/></svg>' for x, y, r, s in pos)
def html(img, off, title, sub):
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
html,body{{margin:0}}.c{{width:540px;height:960px;position:relative;overflow:hidden;font-family:Inter,'DejaVu Sans',Arial,sans-serif;
background:radial-gradient(ellipse at 15% 0%,rgba(20,120,130,.55),transparent 60%),radial-gradient(ellipse at 100% 100%,rgba(194,123,152,.35),transparent 55%),linear-gradient(135deg,#0B5A64,#123A52 55%,#172040)}}
h1{{position:absolute;top:46px;left:0;right:0;text-align:center;margin:0;color:#fff;font-size:38px;line-height:1.15;font-weight:700;letter-spacing:-.5px}}
p{{position:absolute;top:146px;left:24px;right:24px;text-align:center;margin:0;color:#E8C1CE;font-size:19px}}
.ph{{position:absolute;left:80px;top:206px;width:380px;height:800px;background:#0C1220;border-radius:48px;padding:10px;box-shadow:0 24px 60px rgba(0,0,0,.45),inset 0 0 0 2px rgba(255,255,255,.12)}}
.sc{{width:360px;height:780px;border-radius:38px;overflow:hidden;background:#F1F3F2 url(data:image/jpeg;base64,{img}) no-repeat;background-size:360px auto;background-position:center {off}}}
</style></head><body><div class="c">{paws()}<h1>{title}</h1><p>{sub}</p><div class="ph"><div class="sc"></div></div></div></body></html>'''
os.makedirs(OUT, exist_ok=True)
for f in os.listdir(OUT):
    if re.match(r'\d+_.*\.jpg$', f): os.remove(os.path.join(OUT, f))
cells = []
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
    pg = b.new_page(viewport={'width': 540, 'height': 960}, device_scale_factor=2)
    for i, (slug, src, off, title, sub, alt) in enumerate(G, 1):
        img = base64.b64encode(open(f'{SRC}/{src}.jpg', 'rb').read()).decode()
        pg.set_content(html(img, off, title, sub)); pg.wait_for_timeout(200)
        n = f'{i:02d}_{slug}'
        pg.screenshot(path=f'{OUT}/{n}-duzy.jpg', type='jpeg', quality=85)
        Image.open(f'{OUT}/{n}-duzy.jpg').resize((540, 960), Image.LANCZOS).save(f'{OUT}/{n}.jpg', quality=85)
        cells.append(f'<a href="img/{n}-duzy.jpg"><img src="img/{n}.jpg" alt="{alt}" loading="lazy" width="540" height="960"></a>')
    b.close()
p = os.path.join(ROOT, 'index.html'); s = open(p).read()
s = re.sub(r'<div class="shots">.*?</div>', '<div class="shots">' + ''.join(cells) + '</div>', s, count=1, flags=re.S)
open(p, 'w').write(s)
print(len(cells), 'zrzutów')
