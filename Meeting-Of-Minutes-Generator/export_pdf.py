from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

pdf = SimpleDocTemplate("outputs/MoM.pdf")
styles = getSampleStyleSheet()

with open("outputs/MoM.txt", "r", encoding="utf-8") as f:
    content = [Paragraph(f.read().replace("\n", "<br/>"), styles["Normal"])]

pdf.build(content)
print("PDF file created")
