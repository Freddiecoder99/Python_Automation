from excel.read_excel import read_excel
from excel.write_excel import write_excel
from pdf.read_pdf import read_pdf
from pdf.create_pdf import create_pdf

data = read_excel("excel_demo.xlsx")
write_excel([{"Name": "John", "Age": 40}, {"Name": "Jane", "Age": 39}], file_path="output_excel.xlsx")

read_pdf("pdf_sample.pdf")
create_pdf("This is an automated PDF File created using Python!", output_file="generated_pdf.pdf")