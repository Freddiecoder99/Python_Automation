from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font(family="Arial", size=13)
pdf.multi_cell(w=190, h=10, txt="Hello! This is a sample text for testing.\nEnjoy Automation!")
pdf.output("pdf_sample.pdf")