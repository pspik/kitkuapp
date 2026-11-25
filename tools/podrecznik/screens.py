from base import page
T = lambda n: f' data-tap="{n}"'
AV = lambda l, c, s=44: f'<div class="av" style="background:{c};width:{s}px;height:{s}px;font-size:{s*0.42:.0f}px">{l}</div>'
M, P, L = ("M", "#6B4BA6"), ("P", "#A4460C"), ("L", "#0F6E8C")

PHOTO = {"Mruczek": ("pets/mruczek.jpg", "#6B4BA6"), "Pestka": ("pets/pestka.jpg", "#A4460C"), "Luna": ("pets/luna.jpg", "#0F6E8C")}
IMGBASE = "file:///home/claude/kitkuapp/podrecznik/img/"
def petchips(sel, names=("Mruczek", "Pestka", "Luna"), tap=""):
    out = []
    for n in names:
        img, c = PHOTO[n]; on = n == sel
        bg = c if on else c + "29"
        out.append(f'<span style="display:inline-flex;align-items:center;gap:6px;padding:4px 10px 4px 4px;border-radius:999px;background:{bg};color:{"#fff" if on else "#16201C"};font-weight:600;font-size:14px"><img src="{IMGBASE}{img}" style="width:28px;height:28px;border-radius:50%"> {n}</span>')
    return f'<div style="display:flex;gap:6px;margin:8px 0;flex-wrap:wrap"{tap}>' + "".join(out) + "</div>"
S = []

# 1. Pulpit
S.append(("pulpit", "Pulpit", "Pulpit to ekran startowy. Od razu widać, które zwierzaki wymagają uwagi i co trzeba zrobić.", page(f'''
<div class="pad">
 <div class="row"><div class="h1 grow">KitkuApp</div><span class="tb" style="font-size:20px"{T(1)}>🔔</span></div>
 <div class="mut">poniedziałek, 23 listopada 2026</div>
 <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-top:12px">
  <div class="card" style="padding:10px;margin:0"{T(2)}><div class="row">{AV(*M,22)}<span class="b">Mruczek</span></div><div class="mut sm" style="margin:4px 0">8 lat 6 mies.</div><span class="pill over">Zaległe: 2</span></div>
  <div class="card" style="padding:10px;margin:0"><div class="row">{AV(*P,22)}<span class="b">Pestka</span></div><div class="mut sm" style="margin:4px 0">4 lata</div><span class="pill over">Zaległe: 1</span></div>
  <div class="card" style="padding:10px;margin:0"><div class="row">{AV(*L,22)}<span class="b">Luna</span></div><div class="mut sm" style="margin:4px 0">2 lata 3 mies.</div><span class="pill ok">OK</span></div>
 </div>
 <h2>Wymaga uwagi <span class="mut">3 pozycje</span></h2>
 <div class="card"><div class="row" style="align-items:flex-start">{AV(*M)}<div class="grow"><div class="b">Morfologia krwi</div><div class="mut">Ostatnio 02.05.2026 · co 6 mies.</div>
  <div class="row" style="margin-top:8px"><span class="btn"{T(3)}>Dodaj wpis</span><span style="font-size:18px;color:#56635D;margin-left:6px"{T(4)}>🔔</span></div></div><span class="pill over">po terminie</span></div></div>
 <div class="card"><div class="row" style="align-items:flex-start">{AV(*M)}<div class="grow"><div class="b">Kończy się Gastricaid – zapas na 5 dni</div><div class="mut">Zostało 22,5 ml · 4,5 ml dziennie · Mruczek, Pestka</div>
  <div class="row" style="margin-top:8px"><span class="btn"{T(5)}>Leki</span></div></div><span class="pill soon">wkrótce</span></div></div>
 <div class="card"><div class="row" style="align-items:flex-start">{AV(*P)}<div class="grow"><div class="b">Kontrola USG</div><div class="mut">Zalecenie z wizyty 20.05.2026 · termin 20.11.2026</div>
  <div class="row" style="margin-top:8px"><span class="btn o"{T(6)}>Zalecenie</span><span class="btn">Dodaj wpis</span></div></div><span class="pill over">po terminie</span></div></div>
</div>''', "Pulpit"), [
 (1, "Dzwonek otwiera <b>ustawienia przypomnień</b>: co ile miesięcy które badanie, przypomnienia jednorazowe i powiadomienia."),
 (2, "Kafelek zwierzaka otwiera jego <b>profil</b>. Kafelki są ułożone od zwierzaka, który najpilniej wymaga uwagi. „Zaległe” to liczba badań po terminie."),
 (3, "<b>Dodaj wpis</b> otwiera formularz wizyty od razu z właściwym zwierzakiem i badaniem."),
 (4, "Dzwonek przy alercie pokazuje go od razu jako powiadomienie w telefonie – tak to będzie wyglądać."),
 (5, "Alert o kończącym się leku prowadzi do karty <b>Leki</b>, gdzie uzupełnisz zapas."),
 (6, "<b>Zalecenie</b> otwiera wpis z wizyty, z którego pochodzi przypomnienie."),
]))

# 2. Zwierzaki
def catcard(n, sub1, sub2, pill, cls, l, c, tap="", ptap=""):
    return f'''<div class="card" style="padding:14px"{tap}><div class="row"><div class="grow"><div class="b" style="font-size:18px">{n}</div><div class="mut">{sub1}</div><div class="mut">{sub2}</div><div style="margin-top:8px"><span class="pill {cls}">{pill}</span></div></div>
<div style="width:96px;height:96px;border-radius:16px;background:{c};color:#fff;display:flex;align-items:center;justify-content:center;font-size:40px;font-weight:600"{ptap}>{l}</div></div></div>'''
S.append(("zwierzaki", "Zwierzaki", "Lista wszystkich zwierzaków – najpierw te, które pilnie potrzebują badań.", page(f'''
<div class="pad"><div class="row"><div class="h1 grow">Zwierzaki</div><span class="btn"{T(3)}>+ Dodaj zwierzaka</span></div>
 {catcard("Mruczek", "8 lat 6 mies. · ur. 05.2018", "europejski · samiec kastrowany · rudy", "2 do zrobienia", "over", *M, T(1), T(2))}
 {catcard("Pestka", "4 lata · ur. 2022", "syberyjska · samica · szylkretowa", "1 do zrobienia", "over", *P)}
 {catcard("Luna", "2 lata 3 mies. · ur. 08.2024", "pies · beagle · samica", "Aktualne", "ok", *L)}
</div>''', "Zwierzaki"), [
 (1, "Dotknij zwierzaka, aby otworzyć jego <b>profil</b> z podsumowaniem zdrowia, dietą, terminami i historią. Kolejność: najpierw ci, którzy mają najwięcej do zrobienia."),
 (2, "Dotknij zdjęcia, aby <b>wgrać i wykadrować</b> nowe."),
 (3, "<b>+ Dodaj zwierzaka</b>: gatunek (kot albo pies), imię, data urodzenia (dokładna lub przybliżona), rasa, umaszczenie, waga, chip. Dla psa aplikacja stosuje psie normy i przypomnienia."),
]))

# 3. Profil – góra
S.append(("profil", "Profil zwierzaka", "Najważniejsze informacje o zdrowiu jednego zwierzaka.", page(f'''
<div class="pad">
 <div class="top"><span class="back">←</span><span class="sp">Profil kota</span><span{T(1)}>✎</span></div>
 <div class="row" style="gap:16px">{AV("M", "#6B4BA6", 84)}<div><div class="h1" style="margin:0">Mruczek</div><div class="mut">europejski · samiec kastrowany · rudy</div></div></div>
 <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-top:12px">
  <div class="card" style="margin:0;background:#E7EBE9;border:0"><div class="mut sm">Wiek</div><div class="b">8 lat 6 mies.</div></div>
  <div class="card" style="margin:0;background:#E7EBE9;border:0"><div class="mut sm">Urodzony</div><div class="b">05.2018</div></div>
  <div class="card" style="margin:0;background:#E7EBE9;border:0"><div class="mut sm">Waga</div><div class="b">4,8 kg</div></div></div>
 <h2>Stan zdrowia</h2>
 <div class="card"{T(2)}>
  <div class="row" style="align-items:flex-start;margin-bottom:8px"><span class="dot" style="background:#9A3412"></span><div class="grow"><div class="b">Biochemia krwi · 02.11.2026</div><div>podwyższone Kreatynina 2,3 mg/dl (norma 0,8–2,0), SDMA 18 µg/dl (norma 0–14).</div></div><span style="font-size:20px;color:#8A8F8C;align-self:center">›</span></div>
  <div class="row" style="align-items:flex-start"><span class="dot" style="background:#0F6B5C"></span><div>Badanie moczu, Morfologia krwi – w normie.</div></div>
  <div class="mut sm" style="margin-top:8px">Tworzone automatycznie z ostatnich wyników każdego badania.</div></div>
 <div class="card"{T(3)}><div class="row"><span class="b grow">Moje notatki</span>✎</div><div>Źle znosi transport – przed wizytą transporter z kocem.</div></div>
 <h2>Dieta <span class="tb"{T(4)}>+ Dieta</span></h2>
 <div class="card"><div class="row"><span class="b grow">Karma nerkowa</span>✎</div><div class="mut sm">01.09.2026 – na stałe</div><div class="mut sm" style="margin-top:6px">Reakcja na dietę</div><div>Je chętnie, kreatynina stabilna.</div></div>
 <div class="tb" style="margin:2px 4px 0"{T(6)}>Archiwum diet (2)</div>
 <h2>Fizjoterapia <span class="tb"{T(7)}>+ Fizjoterapia</span></h2>
 <div class="card"><div class="row"><span class="b grow">Hydroterapia</span>✎</div><div class="mut sm">10.11.2026 – 15.12.2026</div><div class="mut sm" style="margin-top:6px">Opis zabiegów i efekty</div><div>Bieżnia wodna 2× w tygodniu, lepiej wstaje.</div></div>
 <h2>Terminy badań</h2>
 <div class="card" style="padding:4px 12px">
  <div style="padding:8px 0;border-bottom:1px solid #EDF0EE"{T(5)}><div class="row"><span class="b grow">Morfologia krwi</span><span class="pill over">po terminie</span></div><div class="mut">Ostatnio 02.05.2026 · co 6 mies.</div><div class="bar"><i style="width:100%;background:#C2410C"></i></div></div>
  <div style="padding:8px 0;border-bottom:1px solid #EDF0EE"><div class="row"><span class="b grow">Pomiar ciśnienia</span><span class="pill soon">wkrótce</span></div><div class="mut">Ostatnio 30.05.2026 · co 6 mies.</div><div class="bar"><i style="width:85%;background:#CA8A04"></i></div></div>
  <div style="padding:8px 0"><div class="row"><span class="b grow">USG jamy brzusznej</span><span class="pill ok">w terminie</span></div><div class="mut">Ostatnio 10.03.2026 · co 12 mies.</div><div class="bar"><i style="width:60%;background:#0F6B5C"></i></div></div></div>
</div>''', "Zwierzaki"), [
 (1, "Ołówek otwiera <b>edycję danych</b> zwierzaka (imię, gatunek, data urodzenia, zdjęcie…) i usuwanie."),
 (2, "<b>Stan zdrowia</b> tworzy się sam z najnowszego wyniku każdego badania: na czerwono wartości poza normą (z normą w nawiasie), na zielono badania w normie. Zalecenia typu „kontrola za 12 miesięcy” nie są liczone jako problem. Dotknij pozycji, aby otworzyć badanie."),
 (3, "<b>Moje notatki</b> – dotknij, aby dopisać własne uwagi."),
 (4, "<b>+ Dieta</b>: nazwa, od kiedy, do kiedy lub „na stałe” i reakcja na dietę. W profilu widać tylko trwające diety."),
 (5, "Dotknięcie badania w <b>Terminach</b> filtruje historię poniżej do wpisów z tym badaniem i przewija do niej."),
 (6, "<b>Archiwum diet</b> (pod kartą diety) – zakończone diety (po dacie końca albo po „Zakończ dietę”)."),
 (7, "<b>Fizjoterapia</b> – zabiegi z okresem i opisem efektów, z własną historią (jak diety). Przesuń profil w lewo lub w prawo, aby przejść do kolejnego zwierzaka."),
]))

# 4. Historia
S.append(("historia", "Historia zwierzaka", "Niżej w profilu jest pełna historia wizyt, badań i diet.", page(f'''
<div class="pad">
 <div class="row" style="margin:14px 0 10px"><span style="font-size:20px;font-weight:500">Historia</span>
  <div class="in grow" style="margin:0 8px;padding:10px;color:#56635D"{T(1)}>🔍 kreat</div><span class="btn"{T(2)}>+ Wpis</span></div>
 <div class="mut sm" style="margin-bottom:8px">Znaleziono: 3</div>
 <div class="card"{T(3)}><div class="row" style="align-items:flex-start"><div style="width:56px"><div class="b">02 lis</div><div class="mut">2026</div></div><div class="grow"><div class="b">Biochemia krwi, Profil nerkowy</div><div class="mut">Badanie · wiek 8 lat 6 mies.</div><div style="margin-top:6px"><span class="pill over">2 poza normą</span></div></div></div></div>
 <div class="card" style="border:2px solid #CA8A04"{T(5)}><div class="row" style="align-items:flex-start"><div style="width:56px"><div class="b">20 lis</div><div class="mut">2026</div></div><div class="grow"><div class="b">Kontrola nerek</div><div class="mut">Wizyta · wiek 8 lat 6 mies.</div></div></div>
  <div class="sm" style="color:#9A3412;margin-top:6px">Wizyta się odbyła – uzupełnij wyniki albo dodaj skan z tej wizyty.</div><div class="row" style="margin-top:6px"><span class="btn">Uzupełnij</span><span class="btn o">Dodaj skan</span></div></div>
 <div class="card"><div class="row" style="align-items:flex-start"><div style="width:56px"><div class="b">14 cze</div><div class="mut">2026</div></div><div class="grow"><div class="b">Kontrola nefrologiczna</div><div class="mut">Wizyta · wiek 8 lat 1 mies.</div></div></div></div>
 <div class="row" style="margin:10px 0"{T(4)}><div class="grow" style="height:1px;background:#CBD3CF"></div><span class="mut b" style="padding:0 10px">2025</span><div class="grow" style="height:1px;background:#CBD3CF"></div></div>
 <div class="card"><div class="row" style="align-items:flex-start"><div style="width:56px"><div class="b">18 lis</div><div class="mut">2025</div></div><div class="grow"><div class="b">Biochemia krwi</div><div class="mut">Badanie · wiek 7 lat 6 mies.</div><div style="margin-top:6px"><span class="pill over">1 poza normą</span></div></div></div></div>
</div>''', "Zwierzaki"), [
 (1, "<b>Szukaj</b> filtruje historię na bieżąco – w tytułach, opisach, interpretacjach i lekach. Polskie znaki nie mają znaczenia."),
 (2, "<b>+ Wpis</b> dodaje ręcznie wizytę lub wynik. Data w przyszłości tworzy zaplanowaną wizytę z przypomnieniem."),
 (3, "Dotknij wpisu, aby zobaczyć <b>szczegóły i wyniki</b>. Po cofnięciu wrócisz w to samo miejsce listy."),
 (4, "Kreska z rokiem oddziela wpisy z kolejnych lat."),
 (5, "Wizyta dodana wcześniej z datą w przyszłości, która już się odbyła, jest wyróżniona: <b>Uzupełnij</b> wpisuje wyniki ręcznie, <b>Dodaj skan</b> otwiera import – skan z tego dnia uzupełni ten wpis."),
]))

# 4b. Nowy wpis
S.append(("wpis-nowy", "Nowy wpis", "Ręczny wpis wizyty lub badania – z wynikami, które trafią na wykresy i do stanu zdrowia.", page(f'''
<div class="pad"><div class="top"><span class="back">←</span><span class="sp">Nowy wpis</span><span class="tb">Zapisz</span></div>
 {petchips("Mruczek")}
 <div class="lab">Badania (resetują liczniki)</div>
 <div{T(1)}><div class="row" style="align-items:flex-start;margin-bottom:6px"><span class="mut sm" style="width:72px;padding-top:6px">Krew, mocz</span><div style="display:flex;gap:6px;flex-wrap:wrap;flex:1"><span class="chip">Morfologia</span><span class="chip on">✓ Biochemia</span><span class="chip">Tarczyca</span><span class="chip">Mocz</span></div></div>
 <div class="row" style="align-items:flex-start;margin-bottom:6px"><span class="mut sm" style="width:72px;padding-top:6px">Obrazowe</span><div style="display:flex;gap:6px;flex-wrap:wrap;flex:1"><span class="chip">USG</span><span class="chip">RTG</span><span class="chip">TK</span><span class="chip">Echo serca</span></div></div>
 <div class="row" style="align-items:flex-start"><span class="mut sm" style="width:72px;padding-top:6px">Wizyty</span><div style="display:flex;gap:6px;flex-wrap:wrap;flex:1"><span class="chip">Kontrola</span><span class="chip">Szczepienie</span><span class="chip">Zęby</span><span class="chip">Ciśnienie</span></div></div></div>
 <div class="in" style="margin-top:10px;color:#56635D">Tytuł</div>
 <div class="in" style="margin-top:8px">Kontrola nerek, apetyt dobry.</div>
 <div class="in" style="margin-top:8px"{T(2)}>Kontrola biochemii za 3 miesiące</div>
 <div class="hint" style="margin-top:6px">Przypomnienie: Kontrola biochemii za 3 miesiące (za 3 mies.)</div>
 <h2>Wyniki <span class="tb"{T(3)}>+ Dodaj wynik</span></h2>
 <div class="card"><div class="row"><div class="in grow" style="padding:8px"{T(4)}>Kreat</div><div class="in" style="width:70px;padding:8px;text-align:right">2,4</div><span class="hi" style="width:18px">↑</span><span style="color:#8A8F8C">🗑</span></div>
  <div style="margin-top:6px"><span class="chip" style="font-size:12px;padding:4px 8px">Kreatynina · mg/dl</span></div>
  <div class="row" style="margin-top:6px"{T(5)}><div class="in" style="width:70px;padding:6px;font-size:13px">mg/dl</div><div class="in grow" style="padding:6px;font-size:13px">0,8</div><div class="in grow" style="padding:6px;font-size:13px">2</div></div>
  <div class="mut sm" style="margin-top:4px">Biochemia krwi</div></div>
 <div style="margin-top:6px"><span class="btn" style="display:block;text-align:center"{T(6)}>Zapisz wpis</span></div>
</div>''', "Zwierzaki"), [
 (1, "Zaznacz <b>badania</b> – pogrupowane: krew i mocz, obrazowe, wizyty. Przy badaniach z wynikami (np. biochemia) trzeba podać co najmniej jeden wynik, przy USG, RTG czy echu – opis. Wizyta z datą w przyszłości wymaga tylko tytułu."),
 (2, "<b>Zalecenia</b> osobno od opisu. „Za 3 miesiące” od razu tworzy przypomnienie."),
 (3, "<b>+ Dodaj wynik</b> – kolejny parametr, np. waga, ciśnienie albo wynik krwi."),
 (4, "Pisz nazwę parametru – aplikacja <b>podpowiada</b> parametry z wcześniejszych wyników i wpisuje jednostkę oraz normę. Strzałka ↑/↓ pokazuje wynik poza normą."),
 (5, "Jednostkę i normę możesz zmienić. Nowy parametr przy kilku zaznaczonych badaniach – aplikacja zapyta, do którego należy."),
 (6, "Zapisane wyniki trafiają na <b>wykresy</b> i do <b>stanu zdrowia</b>."),
]))

# 5. Wpis
S.append(("wpis", "Szczegóły wpisu", "Pełny opis wizyty lub badania: wyniki z normami, interpretacja, zalecenia.", page(f'''
<div class="pad">
 <div class="top"><span class="back">←</span><span class="sp">Biochemia krwi</span><span{T(1)}>✎</span></div>
 <div class="mut">02.11.2026 · Badanie · Mruczek · wiek w dniu wizyty: 8 lat 6 mies.</div>
 <h2>Wyniki <span class="chip on" style="font-size:12px;padding:4px 10px"{T(2)}>tylko poza normą</span></h2>
 <div class="card"><div class="b" style="margin-bottom:4px">Biochemia</div><table>
  <tr{T(3)}><td>Kreatynina</td><td class="hi" style="text-align:right">↑ 2,3 mg/dl<div class="mut sm" style="font-weight:400">0,8–2,0</div></td><td style="width:28px;text-align:right">📈</td></tr>
  <tr><td>SDMA</td><td class="hi" style="text-align:right">↑ 18 µg/dl<div class="mut sm" style="font-weight:400">0–14</div></td><td style="text-align:right">📈</td></tr>
  <tr><td>ALT</td><td style="text-align:right">62 U/l<div class="mut sm">10–100</div></td><td style="text-align:right">📈</td></tr></table>
  <div class="tb" style="margin-top:8px"{T(4)}>+ Dodaj brakujący wynik</div></div>
 <h2>Interpretacja</h2><div class="card">Podwyższona kreatynina i SDMA – obraz zgodny z przewlekłą chorobą nerek (IRIS 2).</div>
 <h2>Przypomnienia jednorazowe <span class="tb"{T(5)}>Zmień</span></h2>
 <div class="card"><div class="b">Kontrola biochemii za 3 miesiące</div><div class="mut">Termin: 02.02.2027</div></div>
</div>''', "Zwierzaki"), [
 (1, "Ołówek: <b>edycja wpisu</b> (data, tytuł, opis, waga) albo usunięcie."),
 (2, "Przełącznik pokazuje <b>tylko wyniki poza normą</b> – przydatne przy długich panelach."),
 (3, "Dotknij wyniku, aby go <b>poprawić</b> (wartość, jednostka, norma). 📈 otwiera wykres tego parametru w czasie."),
 (4, "<b>+ Dodaj brakujący wynik</b> – gdy import pominął jakiś parametr."),
 (5, "Przypomnienia wykryte w zaleceniach (np. „kontrola za 3 miesiące”). <b>Zmień</b> prowadzi do ich edycji."),
]))

# 6. Import
S.append(("import", "Import wyników", "Wyniki z PDF-ów i zdjęć z kliniki trafiają do historii bez przepisywania.", page(f'''
<div class="pad"><div class="h1">Dane i ustawienia</div>
 <h2>Import wyników</h2>
 <div class="row"><span class="btn"{T(1)}>Wybierz PDF lub zdjęcia</span><span class="btn o"{T(2)}>Folder z wynikami</span></div>
 <div class="card" style="margin-top:12px"><div class="row">{AV(*M,32)}<div class="grow"><div class="b">Mruczek · 02.11.2026</div><div class="mut sm">Wynik laboratoryjny Vetlab · Biochemia krwi</div></div></div>
  <div class="mut sm" style="margin-top:8px">Wyniki: Biochemia (12) · 2 poza normą</div>
  <div class="mut sm" style="margin-top:8px">WYKRYTE ZALECENIA (odznacz zbędne)</div><div class="row" style="margin-top:4px"><span>☑</span><span>Kontrola biochemii za 3 miesiące · termin: 02.02.2027</span></div>
  <div class="row" style="margin-top:6px"{T(3)}><span>☑</span><span>Przypomnij o kontroli wyników poza normą</span></div>
  <div class="row" style="margin-top:10px;justify-content:flex-end"><span class="tb">Odrzuć</span><span class="btn"{T(4)}>Dodaj do historii</span></div></div>
 <div style="margin-top:4px"><span class="btn o"{T(5)}>Dodaj wszystkie gotowe (3)</span></div>
</div>''', "Dane"), [
 (1, "<b>Wybierz PDF lub zdjęcia</b> – karty wizyt, wyniki z laboratorium, opisy USG, TK, echa serca, skany. Można wybrać wiele plików naraz."),
 (2, "<b>Folder z wynikami</b> – wskaż folder (np. pobrane z poczty), a „Sprawdź nowe” wczyta tylko pliki, których jeszcze nie było."),
 (3, "Gdy są wyniki poza normą, aplikacja może dodać przypomnienie o kontroli za miesiąc."),
 (4, "Sprawdź, czy zwierzak i data się zgadzają, i <b>dodaj do historii</b>. Duplikaty (ten sam zwierzak i dzień) są wykrywane."),
 (5, "<b>Dodaj wszystkie gotowe</b> zapisuje naraz wszystkie rozpoznane dokumenty."),
]))

# 7. Kalendarz
days = ""
import calendar
for wk in calendar.Calendar(0).monthdayscalendar(2026, 11):
    for dd in wk:
        if dd == 0: days += "<div></div>"; continue
        mark = ""
        if dd in (2, 14): mark = '<i style="display:block;width:6px;height:6px;border-radius:50%;background:#0F6B5C;margin:2px auto 0"></i>'
        if dd == 20: mark = '<i style="display:block;width:8px;height:8px;border-radius:50%;border:2px solid #C2410C;margin:1px auto 0"></i>'
        st = "background:#0F6B5C;color:#fff;border-radius:50%;" if dd == 23 else ("background:#DCEBE7;border-radius:12px;" if dd == 14 else "")
        tap = T(3) if dd == 14 else ""
        days += f'<div style="text-align:center;padding:6px 0;{st}"{tap}>{dd}{mark}</div>'
S.append(("kalendarz", "Kalendarz", "Wszystkie wpisy i terminy badań w jednym miejscu.", page(f'''
<div class="pad"><div class="h1">Kalendarz</div>
 {petchips(None, tap=T(1))}
 <div class="card"><div class="row"><span style="font-size:20px">‹</span><span class="grow" style="text-align:center;font-size:18px;font-weight:600"{T(2)}>Listopad 2026 ▾</span><span style="font-size:20px">›</span></div>
  <div style="display:grid;grid-template-columns:repeat(7,1fr);font-size:12px;color:#56635D;text-align:center;margin-top:8px"><div>pn</div><div>wt</div><div>śr</div><div>cz</div><div>pt</div><div>so</div><div>nd</div></div>
  <div style="display:grid;grid-template-columns:repeat(7,1fr);font-size:14px">{days}</div>
  <div class="row mut sm" style="margin-top:8px;gap:14px"><span>● wpis / wizyta</span><span>○ termin badania</span></div></div>
 <h2 style="font-size:16px">14 listopada 2026</h2>
 <div class="card"{T(4)}><div class="row">{AV(*P,32)}<div class="grow"><div class="b">Szczepienie</div><div class="mut sm">Pestka · Wizyta</div></div></div></div>
</div>''', "Kalendarz"), [
 (1, "Filtr zwierzaka – pokaż wszystkie albo tylko jednego."),
 (2, "Dotknij nazwy miesiąca, aby od razu <b>wybrać miesiąc i rok</b>. Strzałki przesuwają o miesiąc."),
 (3, "Dzień z kropką ma wpisy, kółko oznacza termin badania. Dotknięcie dnia pokazuje listę poniżej."),
 (4, "Dotknij wpisu, aby go otworzyć. Po powrocie kalendarz pokaże ten sam miesiąc i dzień."),
]))

# 8. Leki
S.append(("leki", "Leki", "Leki podawane każdemu zwierzakowi, pogrupowane według godzin, i zapasy.", page(f'''
<div class="pad"><div class="h1">Leki</div>
 {petchips("Mruczek", tap=T(1))}
 <h2 style="font-size:16px">08:00</h2>
 <div class="card"><div class="row"><div class="grow"><div class="b">Gastricaid</div><div>1,5 ml</div><div class="mut sm">od 01.10.2026 · na stałe</div><div class="sm" style="color:#0F6B5C">monitorowane zużycie</div></div><span{T(2)}>✎</span><span style="color:#9A3412;margin-left:8px;font-size:18px"{T(3)}>⏹</span></div></div>
 <h2 style="font-size:16px">20:00</h2>
 <div class="card"><div class="row"><div class="grow"><div class="b">Gastricaid</div><div>1,5 ml</div></div><span>✎</span></div></div>
 <div class="card"><div class="row"><div class="grow"><div class="b">Milbemax</div><div>1 szt · co 90 dni</div><div class="sm" style="color:#56635D">następna dawka 12.01.2027</div></div><span>✎</span></div></div>
 <h2>Zapasy – wszystkie zwierzaki <span class="mut sm">stan na 23.11.2026</span></h2>
 <div class="card"{T(4)}><div class="row"><div class="grow"><div class="b">Gastricaid</div><div class="mut">zostało 22,5 ml · 4,5 ml/dzień</div></div><span class="pill over">5 dni</span></div><div class="mut sm">wystarczy do 28.11.2026</div><div class="bar"><i style="width:22%;background:#C2410C"></i></div><div class="mut sm" style="margin-top:6px">Wspólny zapas: Mruczek, Pestka</div></div>
 <h2>Historia diet</h2><div class="card"{T(6)}><div class="b">Eliminacyjna (królik)</div><div class="mut sm">10.02.2026 – 30.04.2026</div><div class="mut sm" style="margin-top:4px">Reakcja na dietę</div><div>Mniej drapania po 4 tygodniach.</div></div>
 <h2>Historia leczenia</h2><div class="card"><div class="b">Prednicortone</div><div class="mut sm">01.06–30.06.2026</div></div>
</div><div style="position:relative"><span class="fab" style="bottom:20px"{T(5)}>+ Dodaj lek</span></div>''', "Leki"), [
 (1, "Wybór zwierzaka – zdjęcie, a w tle kolor zwierzaka (ten sam co na wykresach)."),
 (2, "Ołówek: <b>edycja leku</b> (godzina, dawka, co ile dni, okres, zapas)."),
 (3, "<b>Zakończ podawanie</b> – lek przechodzi do historii leczenia."),
 (4, "<b>Zapasy</b>: ile zostało i na ile dni wystarczy, liczone ze wszystkich zwierzaków dostających ten lek. Dotknij, aby wpisać nową ilość po zakupie. Przy 7 dniach i mniej pojawi się alert na Pulpicie."),
 (5, "<b>+ Dodaj lek</b> otwiera okno nowego leku (następny obrazek)."),
 (6, "<b>Historia diet</b> – zakończone diety zwierzaka z reakcją na dietę (widoczne też w historii profilu)."),
]))

# 9. Okno leku
S.append(("lek-okno", "Nowy lek", "Jeden lek można dodać od razu kilku zwierzakom i o kilku godzinach.", page(f'''
<div class="dlgbg"><div class="dlg"><div class="t">Nowy lek</div>
 <div class="lab">Zwierzaki</div><div style="display:flex;gap:6px;flex-wrap:wrap"{T(1)}><span class="chip on">✓ Mruczek</span><span class="chip on">✓ Pestka</span><span class="chip">Luna</span><span class="chip">Wszystkie</span></div>
 <div class="lab">Godziny podawania</div><div style="display:flex;gap:6px;flex-wrap:wrap"{T(2)}><span class="chip on">✓ 08:00</span><span class="chip">20:00</span><span class="chip">+ Inna godzina</span></div>
 <div class="in" style="margin-top:10px"{T(3)}>Spir</div>
 <div class="mut sm" style="margin-top:6px">Leki już używane:</div><div style="margin-top:4px"><span class="chip">Spirulina · 0,5 g · zapas 80 g</span></div>
 <div class="row" style="margin-top:10px"><div class="in grow">0,5</div><span class="chip">szt</span><span class="chip">ml</span><span class="chip on">g</span></div>
 <div class="mut sm" style="margin-top:4px">Leki dozowane pompką mają zwykle dawkę 1,5 ml, zweryfikuj przed wpisaniem.</div>
 <div class="row" style="margin-top:10px"{T(4)}><span>Podawaj co</span><div class="in" style="width:60px;padding:8px">1</div><span>dzień</span></div>
 <div class="row" style="margin-top:10px"{T(5)}><span style="font-size:18px">☑</span><span>Monitoruj zużycie</span></div>
 <div class="card" style="margin-top:6px"><div class="in">80</div><div class="mut sm" style="margin-top:6px">Aktualny stan wspólnego zapasu. Zmień tylko po zakupie nowego opakowania.</div></div>
 <div class="b" style="color:#0F6B5C;font-size:13px;margin-top:6px">Zostanie dodanych: 2 wpisy (2 × 1).</div>
 <div class="row" style="justify-content:flex-end;margin-top:12px;gap:18px"><span class="tb">Anuluj</span><span class="tb">Zapisz</span></div>
</div></div>''', None), [
 (1, "Zaznacz <b>kilka zwierzaków</b> naraz (albo „Wszystkie”)."),
 (2, "Zaznacz <b>godziny</b> – spośród już używanych albo dodaj inną. Powstanie wpis dla każdej pary zwierzak × godzina."),
 (3, "Przy wpisywaniu nazwy pojawiają się <b>podpowiedzi</b> leków już używanych (także przy literówce). Wybranie podpowiedzi wpisuje dawkę, jednostkę i aktualny zapas."),
 (4, "<b>Podawaj co X dni</b> – np. odrobaczanie co 90 dni."),
 (5, "<b>Monitoruj zużycie</b> – wpisz posiadaną ilość, a aplikacja policzy, na ile dni wystarczy."),
]))

# 10. Wykresy
pts = [(0, 1.6), (1, 1.7), (2, 1.9), (3, 1.8), (4, 2.1), (5, 2.3)]
W, H = 330, 170
def xy(i, v): return 20 + i * (W - 40) / 5, H - 20 - (v - 1.0) / 1.6 * (H - 40)
poly = " ".join(f"{x:.0f},{y:.0f}" for x, y in (xy(i, v) for i, v in pts))
band_top = xy(0, 2.0)[1]; band_bot = xy(0, 0.8 if False else 1.0)[1]
circles = "".join(f'<circle cx="{xy(i,v)[0]:.0f}" cy="{xy(i,v)[1]:.0f}" r="4" fill="{"#C2410C" if v > 2.0 else "#0F6B5C"}"/>' for i, v in pts)
S.append(("wykresy", "Wykresy", "Zmiany wyników w czasie – z zaznaczoną normą.", page(f'''
<div class="pad"><div class="h1">Wykresy</div>
 {petchips("Mruczek", tap=T(1))}
 <div class="card" style="margin-top:10px">
  <div class="row"><span class="chip" style="border-radius:50%;padding:4px 11px"{T(3)}>‹</span><div class="grow" style="text-align:center"{T(2)}><div class="b" style="font-size:17px">Kreatynina <span class="hi">↑</span> <span class="tb">▾</span></div><div class="mut sm">Biochemia krwi · 1 z 12</div></div><span class="chip" style="border-radius:50%;padding:4px 11px">›</span></div>
  <svg width="{W}" height="{H}" style="margin-top:6px"{T(4)}><rect x="0" y="{band_top:.0f}" width="{W}" height="{band_bot-band_top:.0f}" fill="#E1F0EC"/><polyline points="{poly}" fill="none" stroke="#0F6B5C" stroke-width="2"/>{circles}</svg>
  <div class="mut sm"><b style="color:#16201C">lis 2023 – lis 2026</b> · widoczne 5 z 6</div>
  <div class="row" style="margin-top:6px"{T(8)}><span class="mut">−</span><div class="grow" style="height:4px;background:#CFE3DD;border-radius:2px;margin:0 8px;position:relative"><span style="position:absolute;left:22%;top:-7px;width:18px;height:18px;border-radius:50%;background:#0F6B5C"></span></div><span class="mut">+</span></div>
  <div class="row mut sm" style="justify-content:space-between;padding:0 16px"><span>wszystko</span><span>3 mies.</span></div></div>
 <div class="mut sm b" style="margin:12px 0 6px">POZA NORMĄ W OSTATNICH WYNIKACH</div>
 <div style="display:flex;gap:6px;flex-wrap:wrap"{T(5)}><span class="chip on">Kreatynina ↑</span><span class="chip">SDMA ↑</span><span class="chip">Ciśnienie skurczowe ↑</span></div>
 <div class="mut sm b" style="margin:10px 0 6px">PRZYPIĘTE ★</div>
 <div style="display:flex;gap:6px;flex-wrap:wrap"><span class="chip">Waga</span><span class="chip">HCT</span></div>
 <div class="btn o" style="display:block;text-align:center;margin-top:10px"{T(6)}>Wszystkie parametry (38) – szukaj</div>
 <h2>Dodaj pomiar</h2>
 <div class="card"{T(7)}><div class="row" style="gap:8px"><div class="grow mut sm">Data<br><b style="color:#16201C;font-size:14px">24.11.2026</b></div><div class="grow mut sm">Kreatynina (mg/dl)<br><b style="color:#16201C;font-size:14px">&nbsp;</b></div></div><div class="btn" style="display:block;text-align:center;margin-top:8px">Dodaj do wykresu</div></div>
 <h2>Pomiary</h2>
 <div class="card"><table><tr><td>02.11.2026</td><td class="hi" style="text-align:right">2,3</td></tr><tr><td>14.06.2026</td><td class="hi" style="text-align:right">2,1</td></tr><tr><td>18.11.2025</td><td style="text-align:right">1,8</td></tr></table></div>
</div>''', "Wykresy"), [
 (1, "Wybór zwierzaka."),
 (2, "Nazwa parametru – dotknij, aby wybrać inny. Strzałka ↑/↓ oznacza ostatni wynik poza normą."),
 (3, "Strzałki ‹ › przechodzą do poprzedniego / następnego parametru z tej samej grupy (np. kolejne wyniki biochemii)."),
 (4, "Zielony pas to norma, czerwone punkty – wyniki poza normą. Punkty stoją według dat. Przeciągnij wykres w lewo lub w prawo, aby przesunąć widok w czasie; strzałki ‹ › w rogach oznaczają starsze lub nowsze pomiary poza widokiem."),
 (8, "Suwak przybliża wykres – od wszystkich pomiarów do 3 miesięcy. Domyślnie widać ostatnie 3 lata; „↺ Domyślny widok” wraca do tego ustawienia."),
 (5, "Skróty: parametry poza normą w ostatnich wynikach oraz przypięte gwiazdką."),
 (6, "<b>Wszystkie parametry</b> – lista z wyszukiwarką (działa też na inne nazwy, np. „hematokryt” → HCT), pogrupowana jak badania, z ostatnią wartością. Gwiazdka ☆ przypina parametr. Ten sam parametr z różnych laboratoriów jest na jednym wykresie."),
 (7, "<b>Dodaj pomiar</b> – nad listą wcześniejszych pomiarów; np. waga z domowej wagi albo ciśnienie skurczowe zmierzone w domu."),
]))

# 11. Przypomnienia
S.append(("przypomnienia", "Przypomnienia", "Co ile miesięcy które badanie i kiedy dostawać powiadomienia. Otwierane dzwonkiem na Pulpicie.", page(f'''
<div class="pad"><div class="top"><span class="back">←</span><span class="sp">Przypomnienia</span></div>
 <div class="card" style="padding:4px 12px">
  <div class="row" style="padding:10px 0;border-bottom:1px solid #EDF0EE"{T(1)}><div class="grow"><div class="b">Morfologia krwi</div><div class="mut sm">co 6 mies. · śledzone</div></div>✎</div>
  <div class="row" style="padding:10px 0;border-bottom:1px solid #EDF0EE"><div class="grow"><div class="b">Biochemia krwi</div><div class="mut sm">co 6 mies. · śledzone</div></div>✎</div>
  <div class="row" style="padding:10px 0;border-bottom:1px solid #EDF0EE"><div class="grow"><div class="b">USG jamy brzusznej</div><div class="mut sm">co 12 mies. · śledzone</div></div>✎</div>
  <div class="row" style="padding:10px 0"><div class="grow"><div class="b">Pomiar ciśnienia</div><div class="mut sm">co 6 mies. · śledzone</div></div>✎</div></div>
 <div class="tb" style="margin:6px 0"{T(2)}>+ Dodaj własne przypomnienie</div>
 <div class="hint">Częstotliwość badań zależy od zdrowia kota, zweryfikuj zalecenia ze swoim weterynarzem</div>
 <h2>Przypomnienia jednorazowe</h2>
 <div class="card"><div class="row"><div class="grow"><div class="b">Mruczek · Kontrola biochemii za 3 miesiące</div><div class="mut sm">02.02.2027</div></div><span class="tb"{T(3)}>⋮</span></div></div>
 <div class="tb"{T(4)}>+ Dodaj jednorazowe przypomnienie</div>
 <h2>Kiedy przypominać</h2><div class="card"><div class="row"{T(5)}><span class="chip">W dniu terminu</span><span class="chip on">7 dni przed</span><span class="chip">30 dni przed</span></div></div>
</div>''', "Pulpit"), [
 (1, "Dotknij badania, aby zmienić <b>częstotliwość</b>, nazwę, śledzenie albo je usunąć."),
 (2, "Własne przypomnienia – np. odrobaczanie co 3 miesiące."),
 (3, "Przypomnienie jednorazowe: zmień termin, edytuj, przenieś na innego zwierzaka albo usuń."),
 (4, "Nowe przypomnienie jednorazowe – termin datą albo „Za N miesięcy”."),
 (5, "Z jakim wyprzedzeniem badanie ma się pojawiać jako „wkrótce” i w powiadomieniach."),
]))

# 12. Dane i ustawienia
S.append(("dane", "Kopia, wygląd i informacje", "Dalsza część karty „Dane i ustawienia”.", page(f'''
<div class="pad">
 <h2>Eksport — kopia zapasowa</h2>
 <div class="card"><div class="mut sm">Plik kopii</div><div class="b">kitkuapp-kopia.json (Dysk Google)</div><div class="mut sm">Ostatnia kopia: dziś, 08:15</div>
  <div class="row" style="margin-top:8px"{T(1)}><span class="btn o">Nowy plik</span><span class="btn o">Istniejący plik</span></div>
  <div class="row" style="margin-top:8px"{T(2)}><span class="grow">Automatyczna kopia</span><span style="display:inline-block;width:44px;height:26px;border-radius:13px;background:#0F6B5C;position:relative"><i style="position:absolute;right:4px;top:4px;width:18px;height:18px;border-radius:50%;background:#fff"></i></span></div></div>
 <div style="height:1px;background:#E1E6E3;margin-top:24px"></div>
 <h2>Przywracanie</h2><div class="card"><span class="btn o"{T(3)}>Przywróć z pliku kopii…</span></div>
 <div style="height:1px;background:#E1E6E3;margin-top:24px"></div>
 <h2>Wygląd</h2><div class="card"><div class="row"><div class="grow"><div class="b">Ciemny motyw</div><div class="mut sm">Jak w ustawieniach telefonu</div></div><span{T(4)} style="display:inline-block;width:44px;height:26px;border-radius:13px;border:2px solid #56635D;position:relative"><i style="position:absolute;left:4px;top:4px;width:14px;height:14px;border-radius:50%;background:#56635D"></i></span></div></div>
 <h2>O aplikacji</h2><div class="card"><div class="mut">KitkuApp 0.20.2 · <u style="color:#0F6B5C"{T(5)}>lista zmian</u></div><div class="mut" style="margin-top:4px"><u style="color:#0F6B5C">podręcznik użytkownika</u></div><div style="margin-top:8px"><span class="btn o">Polityka prywatności</span></div></div>
</div>''', "Dane"), [
 (1, "Wskaż plik kopii – nowy albo istniejący (np. na Dysku Google). Dane zostają na telefonie i w tym pliku, nigdzie indziej."),
 (2, "<b>Automatyczna kopia</b> zapisuje plik po każdej zmianie danych."),
 (3, "<b>Przywracanie</b> wczytuje dane z kopii – np. na nowym telefonie."),
 (4, "<b>Ciemny motyw</b> – włącz, wyłącz albo zostaw „jak w telefonie”."),
 (5, "Historia zmian aplikacji, podręcznik użytkownika i polityka prywatności."),
]))
