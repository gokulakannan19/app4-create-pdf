import pandas as pd
from fpdf import FPDF

df = pd.read_csv("topics.csv")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():
    pdf.add_page()

    # Set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(255, 0 , 0)
    pdf.cell(w=0, h=12, txt=row["Topic"], ln=1, border=0, align="L")

    # add line
    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)

    # Set the footer                                                                     
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 80, 180)
    pdf.cell(w=0, h=12, txt=row["Topic"], ln=1, border=0, align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # add line
        for y in range(10, 298, 10):
            pdf.line(10, y, 200, y)

        # Set the footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 80, 180)
        pdf.cell(w=0, h=12, txt=row["Topic"], ln=1, border=0, align="R")


pdf.output("output.pdf")