# secspine

secspine ist ein Werkzeugkasten für den Security-Test **eigener, autorisierter**
Anwendungen. Das Rückgrat ist die **Befund-Kette**: vom Verdacht über den reproduzierbaren,
schadensfreien Nachweis bis zur Maßnahme, verbunden über feste IDs und vom Prüfwerkzeug
geprüft. secspine dirigiert fertige Scanner, baut keine eigenen, und wird in die zu testende
Anwendung eingebaut; die Tests laufen dort auf einem eigenen Branch, die Ergebnisse gehen
nach `main`.

## Quickstart

Im Verzeichnis der zu testenden Anwendung ausführen:

```
curl -fsSL https://github.com/flaechsig/secspine/archive/refs/heads/dist.tar.gz | tar -xz --strip-components=1
```

Danach Claude Code im Projekt starten und einen Lauf beginnen:

```
/secspine-scan
```

`secspine-scan` erkennt den Stack selbst, fährt die passenden Scanner (fehlende als
Docker-Container) und legt Befund-Kandidaten an. Weiter mit `/secspine-verify` (bestätigen)
und `/secspine-report` (Bericht). Die Phasen-Skills: `secspine-enum`, `secspine-scan`,
`secspine-verify`, `secspine-triage`, `secspine-report`.

**Aktualisieren:** dieselbe `curl`-Zeile erneut ausführen.

**Voraussetzungen:** Python 3.9 oder neuer (Prüfwerkzeug, nur Standardbibliothek), Git, und
für die Scanner Docker (fehlende laufen als Container); `curl` und `tar` für die Installation.

## Standard & Regeln

Wie ein Befund aufgebaut ist, der Lebenszyklus und die Scanner-Flotte stehen in
`.secspine/STANDARD.md`. Das Prüfwerkzeug: `python3 .secspine/secspine.py {check,render,list,new}`.
Ist die Anwendung ein Projekt mit Agenten-Einstieg (`AGENTS.md`), gehört dort ein kurzer
Verweis auf `.secspine/STANDARD.md` hinein.

## Lizenz

[0BSD](LICENSE): frei nutzbar, kopierbar und änderbar, ohne Bedingungen.

## Dank

secspine dirigiert fertige, frei verfügbare Scanner — Dank und deren Lizenzen in
[ACKNOWLEDGEMENTS.md](ACKNOWLEDGEMENTS.md).
