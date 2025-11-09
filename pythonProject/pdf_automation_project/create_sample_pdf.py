from reportlab.pdfgen import canvas


def create_sample_pdf():
    c = canvas.Canvas("sample.pdf")
    c.drawString(100, 750, "Hello, this is a sample PDF for testing!")
    c.drawString(100, 700, "We are learning how to read PDF with Python.")
    c.save()


create_sample_pdf()
