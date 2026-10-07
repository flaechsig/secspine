# Dank

secspine baut auf der Arbeit anderer auf. Das Prüfwerkzeug selbst nutzt nur die
Python-Standardbibliothek und bündelt keinen fremden Code. Die eigentliche Prüfarbeit
leisten jedoch ausgereifte, frei verfügbare Scanner, die secspine **aufruft** (als lokale
Programme oder als Docker-Container). Großer Dank an die Teams dahinter:

| Werkzeug | Wofür secspine es nutzt | Lizenz |
|---|---|---|
| [Semgrep](https://semgrep.dev) (Community Edition) | Quellcode-Analyse (SAST) | LGPL-2.1 |
| [Trivy](https://trivy.dev) | Abhängigkeiten, Container, Infrastruktur-Konfiguration | Apache-2.0 |
| [gitleaks](https://github.com/gitleaks/gitleaks) | Secrets in der Git-Historie | MIT |
| [OWASP ZAP](https://www.zaproxy.org) | laufende Anwendung / API (DAST) | Apache-2.0 |
| [Nuclei](https://github.com/projectdiscovery/nuclei) | bekannte Lücken per Template | MIT |
| [Nmap](https://nmap.org) | Ports und Dienste | Nmap Public Source License (NPSL, auf GPLv2-Basis) |

Diese Werkzeuge werden nicht mit secspine verteilt; sie bleiben unter ihrer jeweiligen
Lizenz. Wer secspine einsetzt, installiert oder fährt sie selbst (etwa über Docker) und
beachtet dabei deren Lizenzbedingungen — die NPSL von Nmap etwa schränkt die Nutzung in
kommerziellen Produkten ein.

Vorbild für Arbeitsweise und Aufbau ist das Schwesterprojekt
[docspine](https://github.com/flaechsig/docspine).
