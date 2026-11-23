# Strona KitkuApp (GitHub Pages)

- `CHANGELOG.md` – historia wersji aplikacji (najnowsza na górze, format `## X.Y.Z — DD.MM.RRRR` + punkty). Przy każdej nowej wersji aplikacji (repo pspik/Kotki) dopisz krótki wpis dla użytkownika i uruchom `python3 tools/build.py` – zbuduje `zmiany/index.html` i sekcję „Co nowego” w `index.html`.
- `img/` – zrzuty ekranu (mała wersja 540×960 + `-duzy`), galeria w `index.html`. Generuje je `python3 tools/galeria.py` z prawdziwych zrzutów telefonu (dane z fikcyjnej kopii demo) w `tools/galeria-src/` – katalog poza repo; nowe zrzuty dostarcza użytkownik.
- `polityka-prywatnosci/` – polityka prywatności (adres wpisany w aplikacji i w Play Console – nie zmieniać ścieżki).
- `podrecznik/` – podręcznik użytkownika (zrzuty z makiet z fikcyjnymi danymi); generator w `tools/podrecznik/` – przy zmianach ekranów aplikacji zaktualizuj `screens.py` i uruchom `render.py` oraz `build_page.py`.
