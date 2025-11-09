from PyPDF2 import PdfMerger

merger = PdfMerger()
merger.append("sample.pdf")
merger.append("report.pdf")
merger.write("merged.pdf")
merger.close()