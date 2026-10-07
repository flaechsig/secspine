---
name: secspine-run
description: >-
  Standardlauf eines Security-Tests: Scan, Verifikation aller Kandidaten und Bericht in einem
  Zug, ohne Rückfrage, bis zur Frage der Dokumentation. Verwenden, wenn ein Projekt einmal
  durchlaufen werden soll, oder bei Aufruf /secspine-run. Einzelne Phasen: secspine-scan,
  secspine-verify, secspine-report.
---

# secspine-run

Du führst den **Standardlauf** — von Phase zu Phase ohne Rückfrage, bis zu dem einen Punkt, an
dem ein Mensch entscheiden muss. Der Mensch soll am Ende vor **einer** Frage stehen (Übertragung
in die Dokumentation), nicht jede Phase einzeln anstoßen müssen.

## Ablauf

1. **Scope** lesen (`security-review/scope.md`). Fehlt für einen **aktiven** Teil Scope oder
   Freigabe, diesen Teil überspringen und am Ende als offenen Punkt melden — nicht blockieren.
2. **Enumeration** nur, wenn ein laufendes Ziel im Scope ist, sonst überspringen → `secspine-enum`.
3. **Scan** → `secspine-scan`: Kandidaten anlegen.
4. **Verifikation aller Kandidaten** → `secspine-verify` je Kandidat:
   - **Schadensfrei aus der Analyse** (Code lesen, Erreichbarkeit, Konfiguration) wird direkt
     verifiziert — `confirmed` oder `dismissed`.
   - Braucht ein Kandidat einen **aktiven/eingreifenden** Nachweis (Live-Exploit, DAST gegen ein
     laufendes System) oder ein **menschliches Urteil**, wird er **nicht blind ausgeführt**:
     als `candidate` belassen, im Befund als „braucht manuelle Prüfung" vermerkt, weiterlaufen.
5. **Bericht** → `secspine-report`: `check`, dann `render`.
6. **Halt an der Dokumentations-Frage.** Erkennst du eine Architektur-Doku (docspine), schlägst
   du die Übertragung nach Kapitel 11 vor (secspine-report, docspine-Modus) und **wartest auf
   Freigabe**. Ohne Doku sind `security-review/` + Bericht das Ergebnis.

## Am Ende meldest du kurz

- wie viele Funde bestätigt / verworfen,
- welche Kandidaten **noch manuell** zu verifizieren sind (mit Grund),
- was **übersprungen** wurde (fehlender Scope/fehlende Freigabe),
- die offene Entscheidung: Übertragung in die Dokumentation ja/nein.

## Regeln

- **Kein aktiver oder zerstörerischer Nachweis ohne ausdrückliche Freigabe** — im Zweifel
  markieren statt tun. Das ist der „Abbruch vorher" — er wird als Info gemeldet, nicht verschwiegen.
- **Nichts in die Dokumentation schreiben ohne Freigabe** (Schritt 6).
- Einzelne Phasen bleiben einzeln aufrufbar; `secspine-run` ist der bequeme Standardweg.
