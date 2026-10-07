# Changelog

## 0.2

Portscan standardmäßig mit naabu (MIT) statt nmap; nmap bleibt optional für die
Versionserkennung (ADR-0006). Hintergrund: nmaps NPSL schränkt die kommerzielle Nutzung ein,
secspine ist 0BSD. enum-Skill und Scanner-Flotte im Standard nennen naabu zuerst.

## 0.1

Erste ausgelieferte Fassung. Enthält die Befund-Kette (`STANDARD.md`,
`finding-template.md`), das Prüfwerkzeug `secspine.py` (nur Python-Standardbibliothek)
und die Phasen-Skills `secspine-enum`, `secspine-scan`, `secspine-verify`,
`secspine-triage`, `secspine-report`.
