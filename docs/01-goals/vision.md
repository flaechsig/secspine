# Vision

## Kernaussage

Für Developer kleiner, selbst erstellter Anwendungen ist secspine ein Werkzeugkasten
für Security-Tests, der den Weg vom Verdacht zur behobenen, nachgeprüften Schwachstelle
als prüfbare Befund-Kette führt: Jeder Fund bleibt mit fester ID, reproduzierbarem
Nachweis und Maßnahme zusammenhängend. secspine wird in die zu testende Anwendung
eingebaut und auf einem eigenen Branch gefahren; die Ergebnisse gehen per Merge nach main.

## Problem

Scanner liefern viel Lärm und keine durchgängige Spur. Funde verlieren sich zwischen
Werkzeugen, Logs und Notizen; was bestätigt, behoben oder verworfen wurde, ist später
nicht mehr nachvollziehbar. Wer allein oder im kleinen Team eine eigene Anwendung baut,
hat keinen wiederholbaren, belegbaren Security-Testprozess.

## Zielgruppe und Stakeholder

Developer und kleine Teams (bis etwa fünf Personen), die eigene, autorisierte
Anwendungen testen. Stakeholder: wer testet; später, wer den Bericht liest (Audit,
Kunde, das eigene Team).

## Erfolg

- Ein vollständiger Durchlauf — Enumeration, Scan, Verifikation, Bericht — ohne
  Handarbeit am Bericht; der Bericht wird erzeugt.
- Jeder bestätigte Fund trägt Reproduktion und Maßnahme; das Prüfwerkzeug erzwingt das.
- secspine lässt sich in wenigen Minuten in eine Zielanwendung einbauen.
- Ein wiederholter Lauf liefert vergleichbare, nachvollziehbare Befunde.

## Nicht-Ziele

- Kein eigener Scanner: secspine dirigiert fertige Werkzeuge.
- Keine nicht-autorisierten Ziele, kein DoS, nichts Zerstörerisches.
- Kein Ersatz für Security-Wissen, sondern ein Gerüst, das es ordnet.

## Qualitätsziele

- **Schadensfreiheit:** Testen gefährdet nie Daten oder Verfügbarkeit.
- **Nachvollziehbarkeit:** Jeder Fund ist vom Roh-Log bis zum Bericht lückenlos verfolgbar.
- **Portabilität:** Das Prüfwerkzeug nutzt nur die Python-Standardbibliothek; Scanner
  laufen bei Bedarf als Container.

## Themen

Die Vision bricht sich in Epics herunter. Übersicht mit Stories und Status:
[01-goals](README.md).
