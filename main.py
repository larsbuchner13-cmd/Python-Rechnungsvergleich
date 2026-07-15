import pdfplumber


def gesamtbetrag_aus_pdf_lesen(pdf_pfad):
    with pdfplumber.open(pdf_pfad) as pdf:
        erste_seite = pdf.pages[0]
        text = erste_seite.extract_text()

    # Text in einzelne Zeilen zerlegen
    zeilen = text.split("\n")

    # Die Zeile mit dem Gesamtbetrag suchen
    gesamtbetrag_zeile = ""
    for zeile in zeilen:
        if "Gesamtbetrag" in zeile:
            gesamtbetrag_zeile = zeile

    # Aus "Gesamtbetrag: 1.374,45 EUR" den Zahlenteil herausschneiden
    zahlenteil = gesamtbetrag_zeile.split(":")[1]   # " 1.374,45 EUR"
    zahlenteil = zahlenteil.strip()                 # "1.374,45 EUR"
    zahlenteil = zahlenteil.split(" ")[0]           # "1.374,45"

    # Deutsches Zahlenformat in Python-Zahlenformat umwandeln
    zahlenteil = zahlenteil.replace(".", "")        # Tausenderpunkt entfernen -> "1374,45"
    zahlenteil = zahlenteil.replace(",", ".")       # Komma zu Punkt -> "1374.45"

    return float(zahlenteil)


gesamtbetrag_1 = gesamtbetrag_aus_pdf_lesen("rechnungen/rechnung_1.pdf")
gesamtbetrag_2 = gesamtbetrag_aus_pdf_lesen("rechnungen/rechnung_2.pdf")

print("Rechnung 1:", gesamtbetrag_1)
print("Rechnung 2:", gesamtbetrag_2)
