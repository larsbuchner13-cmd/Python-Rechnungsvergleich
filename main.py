import pdfplumber

pdf_pfad = "rechnungen/rechnung_1.pdf"

with pdfplumber.open(pdf_pfad) as pdf:
    erste_seite = pdf.pages[0]
    text = erste_seite.extract_text()

print(text)
