import pdfplumber
from openpyxl import Workbook


def gesamtbetrag_aus_pdf_lesen(pdf_pfad):
    try:
        with pdfplumber.open(pdf_pfad) as pdf:
            erste_seite = pdf.pages[0]
            text = erste_seite.extract_text()
    except FileNotFoundError:
        print(f"Fehler: Datei '{pdf_pfad}' wurde nicht gefunden.")
        return None

    # Text in einzelne Zeilen zerlegen
    zeilen = text.split("\n")

    # Die Zeile mit dem Gesamtbetrag suchen
    gesamtbetrag_zeile = ""
    for zeile in zeilen:
        if "Gesamtbetrag" in zeile:
            gesamtbetrag_zeile = zeile

    if gesamtbetrag_zeile == "":
        print(f"Fehler: In '{pdf_pfad}' wurde keine Zeile mit 'Gesamtbetrag' gefunden.")
        return None

    try:
        # Aus "Gesamtbetrag: 1.374,45 EUR" den Zahlenteil herausschneiden
        zahlenteil = gesamtbetrag_zeile.split(":")[1]   # " 1.374,45 EUR"
        zahlenteil = zahlenteil.strip()                 # "1.374,45 EUR"
        zahlenteil = zahlenteil.split(" ")[0]           # "1.374,45"

        # Deutsches Zahlenformat in Python-Zahlenformat umwandeln
        zahlenteil = zahlenteil.replace(".", "")        # Tausenderpunkt entfernen -> "1374,45"
        zahlenteil = zahlenteil.replace(",", ".")       # Komma zu Punkt -> "1374.45"

        return float(zahlenteil)
    except (IndexError, ValueError):
        print(f"Fehler: Der Betrag in '{pdf_pfad}' konnte nicht gelesen werden.")
        return None


gesamtbetrag_1 = gesamtbetrag_aus_pdf_lesen("rechnungen/rechnung_1.pdf")
gesamtbetrag_2 = gesamtbetrag_aus_pdf_lesen("rechnungen/rechnung_2.pdf")

print("Rechnung 1:", gesamtbetrag_1)
print("Rechnung 2:", gesamtbetrag_2)

if gesamtbetrag_1 is None or gesamtbetrag_2 is None:
    print("Vergleich nicht moeglich, da mindestens ein Betrag nicht gelesen werden konnte.")
else:
    # Betraege vergleichen (mit kleiner Toleranz statt exaktem ==)
    differenz = abs(gesamtbetrag_1 - gesamtbetrag_2)

    if differenz < 0.01:
        ergebnis = "Die Rechnungen stimmen ueberein."
    else:
        ergebnis = f"Achtung: Abweichung von {differenz:.2f} EUR!"

    print(ergebnis)

    # Ergebnis in eine Excel-Datei schreiben
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Rechnungsvergleich"

    sheet.append(["Rechnung", "Gesamtbetrag (EUR)"])
    sheet.append(["Rechnung 1", gesamtbetrag_1])
    sheet.append(["Rechnung 2", gesamtbetrag_2])
    sheet.append(["Ergebnis", ergebnis])

    workbook.save("rechnungsvergleich.xlsx")
    print("Ergebnis gespeichert in 'rechnungsvergleich.xlsx'")
