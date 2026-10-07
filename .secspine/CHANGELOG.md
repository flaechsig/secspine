# Changelog

## 0.4

docspine-Modus (US-0012): `secspine-report` destilliert bestätigte Funde nach Freigabe in
arc42 Kapitel 11 (eigener Abschnitt, Präfix `SEC-`, Status-Spalte), legt Aufträge als Stories
im Epic `E-SECURITY` an und verlinkt beidseitig; behobene Einträge bleiben erhalten.
Installer schützt `logs/` und `certs/` per mitgeliefertem `.gitignore` (auch beim curl-Install).


## 0.3.1

Fix: `render` legt den Ordner `security-review/` an, falls er fehlt (vorher Absturz,
wenn noch kein Befund angelegt war).


## 0.3

Engagement-Ablage mit englischen Namen (docspine-Konvention: Namen englisch, Inhalt in
Projektsprache): Ordner `security-review/` mit `scope.md`, `enumeration.md`, dem generierten
`report.md` und den Befund-Dateien `F-NN.md` in einem Ordner. Das Prüfwerkzeug erkennt
Befunde am ID-Muster. Ersetzt `befunde/` mit `00_scope.md`/`06_bericht.md`.


## 0.2

Portscan standardmäßig mit naabu (MIT) statt nmap; nmap bleibt optional für die
Versionserkennung (ADR-0006). Hintergrund: nmaps NPSL schränkt die kommerzielle Nutzung ein,
secspine ist 0BSD. enum-Skill und Scanner-Flotte im Standard nennen naabu zuerst.

## 0.1

Erste ausgelieferte Fassung. Enthält die Befund-Kette (`STANDARD.md`,
`finding-template.md`), das Prüfwerkzeug `secspine.py` (nur Python-Standardbibliothek)
und die Phasen-Skills `secspine-enum`, `secspine-scan`, `secspine-verify`,
`secspine-triage`, `secspine-report`.
