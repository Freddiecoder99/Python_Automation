from reportlab.pdfgen import canvas


def create_report_pdf():
    c = canvas.Canvas("report.pdf")
    c.drawString(100, 750, "This is the second report PDF.")
    c.drawString(100, 700, "We will merge this with the sample PDF.")
    c.save()


create_report_pdf()
