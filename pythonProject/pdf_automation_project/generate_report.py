from reportlab.pdfgen import canvas

c = canvas.Canvas("generate_report.pdf")
c.drawString(100, 750, "This is a generated PDF report using Python.")
c.save()