# AGENTS.md

Einstieg für KI-Agenten in dieses Repo.

## Was das hier ist

secspine ist ein Werkzeugkasten für Security-Tests eigener, autorisierter Anwendungen.
Rückgrat ist die Befund-Kette: vom Verdacht über den Nachweis bis zur Maßnahme, verbunden
über feste IDs.

## Dokumentation (docspine)

Dieses Projekt dokumentiert sich nach docspine.

- `docs/README.md`: wie mit der Doku gearbeitet wird
- `.docspine/STANDARD.md`: die Regeln
- `.docspine/PROFILE.md`: Projektwerte und Abweichungen
- `docs/01-goals/README.md`: Übersicht aller Epics und Stories mit Status

Vor jedem Commit, spätestens vor dem Merge, in dieser Reihenfolge prüfen:

```
# noch keine Tests — mit docspine-gate Build und erste Tests anbinden,
# damit sie von Anfang an mit docspine verbunden sind
python3 .docspine/docspine.pyz render
python3 .docspine/docspine.pyz check --without-tests
```

## Das Werkzeug secspine selbst

Produkt-Payload liegt unter `.secspine/` (Standard, Prüfwerkzeug, Vorlage) und
`.agents/skills/secspine-*` (die Phasen-Skills). Das ist der Gegenstand der Entwicklung,
nicht die docspine-Konfiguration.
