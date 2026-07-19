# Python-Rechnungsvergleich

Kleines Tool, das zwei PDF-Rechnungen einliest, deren Gesamtbeträge vergleicht
und das Ergebnis in eine Excel-Datei schreibt.

## Setup (Windows)

1. Repository herunterladen/klonen und im Ordner öffnen.
2. Virtuelle Umgebung erstellen:
   ```
   python -m venv venv
   ```
3. Virtuelle Umgebung aktivieren:
   ```
   venv\Scripts\activate
   ```
4. Abhängigkeiten installieren:
   ```
   pip install -r requirements.txt
   ```

## Ausführen

```
python main.py
```

Das Skript liest `rechnungen/rechnung_1.pdf` und `rechnungen/rechnung_2.pdf`
ein, vergleicht die jeweiligen Gesamtbeträge und schreibt das Ergebnis in
`rechnungsvergleich.xlsx` im Projektordner.

## Eigene Rechnungen verwenden

Die beiden PDF-Dateien in `rechnungen/` sind aktuell nur Beispiel-Rechnungen.
Um eigene Rechnungen zu vergleichen, die Dateien in `rechnungen/` ersetzen
(gleicher Dateiname) oder die Pfade in `main.py` anpassen.

**Voraussetzung:** Die PDF muss eine Zeile enthalten, die mit
`Gesamtbetrag: <Betrag> EUR` beginnt (deutsches Zahlenformat, z.B.
`1.374,45`). Bei anderem Format meldet das Skript einen Fehler statt
abzustürzen.
