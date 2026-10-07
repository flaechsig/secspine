---
name: sec-scan
description: >-
  Phase 3 des Pentests (Schwachstellenanalyse): die Scanner-Flotte gegen ein eigenes,
  autorisiertes Ziel fahren — SAST (Semgrep), Abhängigkeiten/Container/IaC (Trivy), Secrets
  (gitleaks), laufende App/API (OWASP ZAP), bekannte Lücken (Nuclei) — Roh-Output nach logs/,
  je echtem Verdacht einen Befund-Kandidaten in befunde/findings/ anlegen. Wählt die Scanner
  passend zum Stack selbst und fährt fehlende als Docker-Container. Verwenden nach sec-enum
  oder bei Aufruf /sec-scan.
---

# sec-scan

Du dirigierst fertige Scanner gegen ein **eigenes, autorisiertes** Ziel und machst aus ihren
Treffern **Kandidaten** (`status: candidate`), keine fertigen Befunde. Scope in
`befunde/00_scope.md` zuerst lesen; nur im Scope scannen.

## Config selbst finden (nicht fragen)

- **Stack erkennen**: nach Quellcode, `Dockerfile`, `package.json`/`pom.xml`/`requirements.txt`,
  IaC (`*.tf`, k8s-YAML) sehen → welche Scanner sinnvoll sind.
- **Läuft das Ziel?** Offene Ports aus `befunde/02_enumeration.md` → wenn eine Web-App/API
  erreichbar ist, kommt DAST (ZAP) dazu.
- **Was ist lokal da?** `command -v` für `semgrep trivy gitleaks nuclei`. Fehlt einer und
  `docker` ist da, fahr ihn als Container (z. B. `returntocorp/semgrep`, `aquasec/trivy`,
  `zricethezav/gitleaks`, `projectdiscovery/nuclei`, `ghcr.io/zaproxy/zaproxy`).

## Flotte

| Scanner | Wogegen | Log |
|---|---|---|
| Semgrep | Quellcode (SAST) | `logs/03_semgrep_<datum>.txt` |
| Trivy | Abhängigkeiten, Images, IaC | `logs/03_trivy_<datum>.txt` |
| gitleaks | Secrets in der Git-Historie | `logs/03_gitleaks_<datum>.txt` |
| ZAP Baseline | laufende App/API (DAST) | `logs/03_zap_<datum>.txt` |
| Nuclei | bekannte Lücken (Templates) | `logs/03_nuclei_<datum>.txt` |

Lange Läufe (ZAP Full, Nuclei komplett) sind Nachtlauf-Kandidaten — hier die schnellen
Varianten (Baseline), die Vollläufe später automatisiert.

## Aus Treffern Kandidaten machen

1. Roh-Output **immer** nach `logs/`, unverändert.
2. Scanner-Treffer sichten: Dubletten und offensichtliche False Positives zusammenfassen.
   Nicht jeden Scanner-Eintrag zum Befund machen — das ist Lärm.
3. Je echtem, eigenständigem Verdacht:
   `python3 .secspine/secspine.py new F-NN "<Titel>"`, dann Frontmatter füllen
   (`status: candidate`, `severity`, `target`, `source: <scanner>`, `evidence: [logs/…]`,
   wenn bekannt `cwe`/`owasp`) und den Abschnitt `## Was` schreiben. Repro/Auswirkung/Maßnahme
   bleiben für `sec-verify`.
4. Am Ende `python3 .secspine/secspine.py check` — muss OK melden.

## Regeln

- Scanner gegen Produktion nur mit Freigabe und schonend (Baseline, kein aktiver Angriffs-Scan).
- Treffer sind Verdacht, nicht Wahrheit. Bestätigt wird in Phase 4 (`sec-verify`).
- Nächste freie `F-`Nummer nehmen; `check` meldet Doppelungen.
