# secspine

secspine ist ein Werkzeugkasten für den Security-Test **eigener, autorisierter**
Anwendungen — gebaut nach dem Vorbild von [docspine](https://github.com/flaechsig/docspine).
Das Rückgrat ist die **Befund-Kette**: von einem Verdacht über den reproduzierbaren,
schadensfreien Nachweis und die Auswirkung bis zur Maßnahme, verbunden über eine feste ID
und vom Prüfwerkzeug geprüft.

secspine verhält sich zum Security-Test wie docspine zur Entwicklung: dieselbe Arbeitsweise
(feste IDs, Gates, Branch mit Merge nach `main`), anderes Rückgrat. Es wird in die zu
testende Anwendung installiert; die Tests laufen dort auf einem eigenen Branch, die
Ergebnisse werden nach `main` gemergt.

## Teile

- **Standard & Regeln:** [`.secspine/STANDARD.md`](.secspine/STANDARD.md) — Befund,
  Lebenszyklus, IDs, Scanner-Flotte.
- **Prüfwerkzeug:** `python3 .secspine/secspine.py {check,render,list,new}` (nur
  Python-Standardbibliothek).
- **Skills** (unter `.agents/skills/`, offener Agent-Skills-Standard):
  `secspine-enum` (Enumeration) · `secspine-scan` (Scanner-Flotte) · `secspine-verify` (Verifikation) ·
  `secspine-triage` (nach einem Scan-Lauf) · `secspine-report` (Bericht).

## Stand

Junges Projekt, unter docspine aufgesetzt: Vision, Ziele, Entscheidungen und erste Stories
stehen in `docs/`. Als Nächstes u. a. ein `curl`-Installationsweg (US-0006).

## Lizenz

[0BSD](LICENSE): Jeder darf secspine ohne Bedingungen nutzen, kopieren, ändern und
weitergeben.

## Dank

secspine dirigiert fertige, frei verfügbare Scanner, statt eigene zu bauen. Dank an die
Teams dahinter — Werkzeuge und ihre Lizenzen in [ACKNOWLEDGEMENTS.md](ACKNOWLEDGEMENTS.md).
