# Historia zmian KitkuApp

## 0.21.1 — 25.11.2026
- Ocena bólu: ekran mieści się nad paskiem nawigacji telefonu – przycisk „Zapisz” jest zawsze dostępny; krótszy komunikat o progu bólu.

## 0.21.0 — 25.11.2026
- Nowy pomiar domowy dla kotów: „Ocena bólu (mimika)” według Feline Grimace Scale – 5 cech pyszczka (uszy, oczy, pyszczek, wąsy, głowa) z ilustracjami 0 / 1 / 2.
- Cechę, której nie widać, można pominąć (najwyżej 2) – wynik przeliczy się do skali 0–10.
- Wynik trafia na wykres; od 4/10 jest poza normą, a aplikacja przypomina o kontakcie z lekarzem weterynarii.

## 0.20.2 — 25.11.2026
- O aplikacji: pod linkiem do listy zmian jest link do podręcznika użytkownika.

## 0.20.1 — 24.11.2026
- Wykresy: „Dodaj pomiar” jest teraz nad listą wcześniejszych pomiarów.
- Pomiary domowe: usunięte ciśnienie rozkurczowe (u kotów ocenia się głównie skurczowe). Wartości rozkurczowe z wypisów nadal są na wykresach.

## 0.20.0 — 24.11.2026
- Wykresy na osi czasu: punkty w odstępach zgodnych z datami, na osi lata (po przybliżeniu półrocza i kwartały).
- Domyślnie widać ostatnie 3 lata; gdy pomiary obejmują krótszy okres – wszystkie.
- Przeciągnięcie wykresu w lewo lub w prawo przesuwa widok w czasie; strzałki ‹ › w rogach pokazują, że są starsze lub nowsze pomiary.
- Suwak pod wykresem przybliża od „wszystko” do 3 miesięcy; „↺ Domyślny widok” wraca do 3 lat.

## 0.19.2 — 24.11.2026
- Wykresy: parametry morfologii w kolejności jak na wydruku z analizatora (WBC, BAS%, BAS, NEU%, NEU … PLT, MPV, PDW, PCT), pozostałe pod nimi alfabetycznie.

## 0.19.1 — 24.11.2026
- Wykresy: ten sam wynik zapisany w dwóch dokumentach z jednego dnia pokazuje się raz (bez nakładających się etykiet).
- Parametry podawane w % (np. NEU %) mają własny wykres, osobno od wartości bezwzględnych.
- Lista parametrów: bez pustych dopisków „też:”.

## 0.19.0 — 24.11.2026
- Wykresy: wykres od razu pod wyborem zwierzaka. Dotknięcie nazwy parametru otwiera wybór, strzałki ‹ › przechodzą do sąsiednich parametrów z tej samej grupy.
- Pod wykresem skróty: parametry poza normą w ostatnich wynikach i przypięte gwiazdką.
- „Wszystkie parametry” – lista z wyszukiwarką (także po innych nazwach, np. „hematokryt”), pogrupowana jak badania, z ostatnią wartością.
- Ten sam parametr z różnych laboratoriów (np. HCT i Hematokryt, PLT i Płytki krwi) oraz nazwy rozbite przy odczycie PDF trafiają na jeden wykres.

## 0.18.2 — 24.11.2026
- Profil: „Archiwum diet” i „Historia fizjoterapii” przeniesione pod karty – przycisk dodawania w nagłówku nie łamie się już na wąskich ekranach.

## 0.18.1 — 23.11.2026
- Poprawka: po przesunięciu profilu na innego zwierzaka „Terminy badań” pokazywały daty poprzednio oglądanego zwierzaka.

## 0.18.0 — 23.11.2026
- Wizyta z datą w przyszłości wymaga tylko tytułu. Gdy termin minie, jest wyróżniona w historii i na Pulpicie z prośbą o wyniki – „Uzupełnij” albo „Dodaj skan” (skan z tego dnia uzupełni ten wpis).
- Dieta: w profilu tylko trwające diety, zakończone w „Archiwum diet”. „Zakończ dietę” od razu przenosi ją do archiwum.
- Fizjoterapia przeniesiona z kategorii badań do profilu zwierzaka – sekcja pod dietą, z własną historią.
- Przesunięcie profilu w lewo lub w prawo przechodzi do kolejnego zwierzaka.
- Kategorie badań przy dodawaniu wpisu pogrupowane (krew i mocz, obrazowe, wizyty) i zajmują mniej miejsca.

## 0.17.0 — 23.11.2026
- Ręczny wpis: osobne pola Opis i Zalecenia (zalecenia tworzą przypomnienia), wyniki wpisywane wierszami – z podpowiedzią parametru, jednostką, normą i strzałką poza normą. Badanie z wynikami wymaga co najmniej jednego wyniku. Wyniki trafiają na wykresy i do stanu zdrowia.
- Nowa kategoria: Fizjoterapia (opis zabiegów i zalecenia).
- Stan zdrowia: dotknięcie pozycji otwiera badanie, przy wartościach poza normą widać normę, a zalecenia typu „kontrola za 12 miesięcy” nie są liczone jako problem.
- Wybór zwierzaka ze zdjęciem i kolorem zwierzaka w tle (kalendarz, leki, wykresy, wpisy).
- Leki: sekcja „Historia diet” nad historią leczenia.

## 0.16.0 — 23.11.2026
- Profil zwierzaka: sekcja „Dieta” (nazwa, od–do lub na stałe, reakcja na dietę). Po zakończeniu dieta przechodzi do historii.
- Wyszukiwanie w historii zwierzaka – w tytułach i opisach wpisów, na bieżąco podczas pisania.
- Historia podzielona na roczniki – kreska z rokiem na granicy lat.
- Po powrocie z otwartego wpisu profil wraca w to samo miejsce historii.

## 0.15.2 — 23.11.2026
- Lepszy import historii wizyt: opis badania klinicznego zachowuje podział na punkty, zawinięte zdania są sklejane, a wizyty z samymi załącznikami są pomijane.
- Poprawnie odczytywane wyniki, w których wartość jest sklejona z nazwą parametru (np. SAA), wyniki „w toku” są pomijane, a „Wartość” dostaje nazwę badania.
- Interpretacja wyniku przerwana podziałem strony nie gubi ostatniego zdania.

## 0.15.1 — 23.11.2026
- Nowa ikona aplikacji.
- Zakładka „Dane i ustawienia” – czytelniej rozdzielone sekcje przywracania kopii i wyglądu.

## 0.15.0 — 22.11.2026
- Normy badania moczu dla kotów i psów, gdy laboratorium ich nie podało: ciężar właściwy, pH, stosunek białko/kreatynina (z rozróżnieniem wartości granicznej i białkomoczu), erytrocyty i leukocyty w osadzie.
- Wyniki opisowe (glukoza, ketony, krew, bilirubina, bakterie, wałeczki, nabłonki, liczne kryształy) oznaczane jako nieprawidłowe, z normą słowną obok. Białko z paska u kota – tylko informacyjnie.
- Nieprawidłowe wyniki moczu trafiają do podsumowania stanu zdrowia.

## 0.14.0 — 22.11.2026
- Ciemny motyw: przełącznik w zakładce Dane (sekcja „Wygląd”). Domyślnie aplikacja dopasowuje się do ustawień telefonu.

## 0.13.1 — 22.11.2026
- Lepszy import zeskanowanych kart wizyt: rozpoznawane sekcje „Opis badania”, „Zabiegi” i „Zastosowane leki” mimo ikon przy nagłówkach, a także data wizyty zaznaczona zakreślaczem.
- Tomografia wpisana w zabiegach oznacza wpis kategorią TK.

## 0.13.0 — 22.11.2026
- Profil zwierzaka: nowa sekcja „Stan zdrowia” – podsumowanie tworzone automatycznie z ostatnich wyników każdego badania (wartości poza normą, wnioski z badań obrazowych, na końcu badania w normie). Odświeża się samo po dodaniu nowych wyników.
- Pod podsumowaniem pole „Moje notatki” na własne uwagi o zdrowiu.

## 0.12.5 — 22.11.2026
- Import opisów tomografii komputerowej: rozpoznawane imię zwierzęcia, data i tytuł badania, lekarz opisujący i kierujący, a do wpisu trafia pełny opis i wnioski (bez stopek i stron z obrazami).
- Nowa kategoria badań: Tomografia komputerowa.

## 0.12.4 — 22.11.2026
- Kalendarz: dotknięcie nazwy miesiąca otwiera wybór miesiąca i roku.
- Kalendarz: usunięta karta „Terminy badań” – terminy są w profilach zwierzaków, a w widoku miesiąca nadal widać je jako kółka.
- Po powrocie z otwartego wpisu kalendarz pokazuje ten sam miesiąc, dzień i filtr.

## 0.12.3 — 22.11.2026
- Leki podawane co kilka dni: w oknie leku pole „Podawaj co … dni”, na liście informacja o następnej dawce, a zapasy liczą zużycie tylko w dni podania.

## 0.12.2 — 22.11.2026
- Sekcja Zapasy na karcie Leki pokazuje wszystkie monitorowane leki, niezależnie od wybranego zwierzaka, razem z informacją, kto je dostaje.

## 0.12.1 — 22.11.2026
- W przypomnieniu jednorazowym termin można ustawić wpisując „Za … miesięcy” – data przelicza się sama.

## 0.12.0 — 22.11.2026
- Zapasy leków: zaznacz „Monitoruj zużycie”, wpisz posiadaną ilość, a karta Leki pokaże, na ile dni wystarczy zapas. Zużycie liczone jest ze wszystkich zwierzaków, które dostają ten sam lek.
- Przypomnienie na Pulpicie i powiadomienie, gdy zapas leku kończy się w ciągu 7 dni.
- Dawka wpisywana jako liczba z jednostką (szt, ml, g).
- Nowy lek można dodać od razu kilku zwierzakom i o kilku godzinach.
- Podpowiedzi nazw leków już używanych (także przy literówce) – z dawką i jednostką.

## 0.11.6 — 20.11.2026
- Opisy badań USG importowane w całości, w akapitach, z kategorią „USG jamy brzusznej”.
- Poprawione rozpoznawanie imion i słów w wypisach, w których PDF rozdzielał wyrazy (np. „Zw ierzę”).

## 0.11.5 — 20.11.2026
- Uwaga o konsultacji częstotliwości badań z weterynarzem przeniesiona nad przypomnienia jednorazowe.
- W zakładce Dane przy numerze wersji link do listy zmian.

## 0.11.4 — 20.11.2026
- Przypomnienie o USG jamy brzusznej domyślnie co 12 miesięcy (wcześniej 6).
- W ustawieniach przypomnień uwaga, że częstotliwość badań warto ustalić z lekarzem weterynarii.

## 0.11.3 — 20.11.2026
- Przypomnienie o echu serca domyślnie co 12 miesięcy (wcześniej 24), zgodnie z zaleceniem corocznej kontroli kotów z ras predysponowanych i z łagodną kardiomiopatią.

## 0.11.2 — 19.11.2026
- Przy dodawaniu wpisu i imporcie nie trzeba już wybierać rodzaju (wizyta, badanie, telefon, pomiar domowy) — aplikacja ustawia go sama.

## 0.11.1 — 19.11.2026
- Profil zwierzaka: dotknięcie badania w „Terminach badań” pokazuje historię tylko z tym badaniem.

## 0.11.0 — 19.11.2026
- Import wypisów z gabinetu kardiologicznego: cały wynik echa serca zapisany w opisie wizyty, wywiad, waga, ciśnienie i zalecenia (np. kontrolne echo po 3–4 miesiącach).
- Imię z wypisu dopasowywane mimo drobnej różnicy w pisowni (np. Papaya ↔ Papaja).

## 0.10.6 — 19.11.2026
- Numer wersji rośnie automatycznie z każdym wydaniem (porządek przy publikacji w Google Play).

## 0.10.5 — 19.11.2026
- Polityka prywatności na stronie aplikacji (GitHub Pages), link w zakładce Dane.

## 0.10.4 — 18.11.2026
- Import kilku dużych kartotek naraz bez zawieszania aplikacji: zapis w tle, pliki czytane po kolei, lista wizyt pokazywana porcjami, przycisk usuwania duplikatów z listy.

## 0.10.3 — 17.11.2026
- Edycja i usuwanie przypomnień: zmiana nazwy i okresu, usuwanie własnych i domyślnych (z możliwością przywrócenia), edycja przypomnień jednorazowych.

## 0.10.2 — 17.11.2026
- Zwierzaki na Pulpicie i w zakładce Zwierzaki ułożone od tych, które najbardziej potrzebują badań.
- Terminy badań w profilu od zaległych do najodleglejszych.
- Leki pogrupowane według godziny podawania.

## 0.10.1 — 17.11.2026
- Nowe przypomnienie: pomiar ciśnienia co 6 miesięcy.

## 0.10.0 — 17.11.2026
- Przygotowanie do Google Play: nowy identyfikator aplikacji, Android 16, polityka prywatności.

## 0.9.2 — 17.11.2026
- Przypomnienia jednorazowe nie mnożą się po imporcie starszych kartotek; zamknięte można ukryć lub usunąć.

## 0.9.1 — 17.11.2026
- Ręczna poprawa zaimportowanych wyników: nazwa, wartość, jednostka, norma, dodawanie i usuwanie pozycji.
- Poprawny tytuł badania, gdy tabela zaczyna się na następnej stronie wypisu.

## 0.9.0 — 17.11.2026
- Psy obok kotów, z typowymi wartościami tętna, oddechów i ciśnienia dla psa.
- Przypomnienia jednorazowe z zaleceń w wypisie (np. „powtórzyć USG za miesiąc”) i po wynikach poza normą.

## 0.8.0 — 17.11.2026
- Zdjęcia zwierząt z przesuwaniem i kadrowaniem.
- Ciśnienie skurczowe, rozkurczowe i tętno w pomiarach domowych i z wypisów.

## 0.7 — 17.11.2026
- Nowa zakładka Leki: godzina podawania, dawka, uwagi, daty oraz historia leczenia.
- Czytelniejszy dolny pasek nawigacji.

## 0.6 — 17.11.2026
- Nowa nazwa: KitkuApp, przycisk „Postaw kotkom karmę”.
- Przypomnienie o echu serca (co 24 miesiące) i własne przypomnienia.

## 0.5 — 17.11.2026
- Odczyt skanów PDF i zdjęć wypisów (rozpoznawanie tekstu w telefonie).
- Pomiary domowe: oddechy w spoczynku, biegunka, wymioty; zwijane kategorie wykresów.
- Zakładka Dane z importem i kopią zapasową, dzwonek do ustawień przypomnień, do 6 zwierzaków widocznych bez przewijania.

## 0.4 — 16.11.2026
- Import zbiorczych wypisów z wieloma wizytami w jednym pliku.
- Jednostki wyników przeliczane na wspólne, dokładniejszy odczyt tabel z wynikami.

## 0.3 — 16.11.2026
- Pierwsza wersja: kalendarz badań z przypomnieniami, profile kotów z wiekiem, import wypisów PDF, wykresy wyników, kopia zapasowa na Dysku Google.
