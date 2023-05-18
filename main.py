from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P",unit="mm",format="A4")

df= pd.read_csv("topics.csv")

for index,row in df.iterrows():
        pdf.add_page()
        pdf.set_font(family="Times",style="B",size=24)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=0,h=12,txt=row["Topic"], align="L",ln=1)
        pdf.line(10,20,200,20)

        for i in range(10,250,10):
                pdf.line(10, i+20, 200, i+20)

        pdf.ln(240)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.cell(w=0,h=10,txt=row["Topic"], align="R")
        pdf.set_text_color(180,180,180)
        for i in range(row["Pages"]-1):
            pdf.add_page()
            for k in range(10, 240, 10):
                    pdf.line(10, k + 20, 200, k + 20)
            pdf.ln(240)
            pdf.set_font(family="Times", style="I", size=8)
            pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
            pdf.set_text_color(180, 180, 180)





pdf.output("output.pdf")
