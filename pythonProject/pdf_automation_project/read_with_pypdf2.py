import PyPDF2

with open('sample.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    print(f"Total Pages: {len(reader.pages)}")

    for i in range(len(reader.pages)):
        page = reader.pages[i]
        text = page.extract_text()
        print(f"\n--- Page {i+1} ---\n{text}")