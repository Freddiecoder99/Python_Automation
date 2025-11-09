import pdfplumber

with pdfplumber.open('sample.pdf') as pdf:
    for i, page in enumerate(pdf.pages):
        text = page.extract_text()
        print(f"\n--- Page {i+1} ---\n{text}")