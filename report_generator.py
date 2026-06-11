from reportlab.pdfgen import canvas
from datetime import datetime

def generate_report(
    disease,
    recommendation
):

    filename = "Farmer_Report.pdf"

    c = canvas.Canvas(filename)

    c.setFont("Helvetica-Bold", 18)
    c.drawString(150, 800, "AgriSense AI Report")

    c.setFont("Helvetica", 12)

    c.drawString(
        50,
        750,
        f"Date: {datetime.now()}"
    )

    c.drawString(
        50,
        700,
        f"Disease: {disease}"
    )

    c.drawString(
        50,
        650,
        f"Recommendation: {recommendation}"
    )

    c.save()

    return filename