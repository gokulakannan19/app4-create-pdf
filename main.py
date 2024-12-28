from fpdf import FPDF

pdf = FPDF(orientation="L", unit="mm", format="A4")

pdf.add_page()
pdf.set_font(family="Times", style="B", size=12)
pdf.cell(w=0, h=12, txt="Hi there", ln=1, border=1, align="L")
pdf.cell(w=0, h=12, txt="Hello there", ln=1, border=1, align="L")


pdf.add_page()
pdf.set_font(family="Times", style="B", size=12)
pdf.cell(w=0, h=12, txt="Hi there", ln=1, border=1, align="L")
pdf.cell(w=0, h=12, txt="Hello there", ln=1, border=1, align="L")

pdf.output("output.pdf")