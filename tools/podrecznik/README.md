# Podręcznik użytkownika – generator

Zrzuty ekranów to makiety HTML z fikcyjnymi danymi (`screens.py`, style w `base.py`).
Elementy oznaczone `data-tap="n"` dostają numerowane znaczniki kliknięć.

    cd tools/podrecznik
    python3 render.py      # zrzuty → podrecznik/img/*.jpg + meta.json (Playwright + Chrome)
    python3 build_page.py  # podrecznik/index.html

Po zmianach w aplikacji zaktualizuj odpowiedni ekran w `screens.py`.
