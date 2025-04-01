# pdf_generator.py

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

def generate_preset_pdf(preset, filename="preset.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    y = height - 50
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, f"Preset : {preset['bassiste']}")

    y -= 30
    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Généré le : {datetime.now().strftime('%d/%m/%Y %H:%M')}")

    y -= 40
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Basse")
    y = draw_dict_block(c, preset["basse"], y)

    y -= 20
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Ampli")
    y = draw_dict_block(c, preset["ampli"], y)

    y -= 20
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Effets")
    for effet, reglages in preset["effets"].items():
        y -= 20
        c.setFont("Helvetica-Bold", 12)
        c.drawString(60, y, effet)
        y = draw_dict_block(c, reglages, y, indent=80)

    y -= 20
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Baffle")
    y = draw_dict_block(c, preset["baffle"], y)

    y -= 20
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Chaîne du signal")
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(60, y, " ➔ ".join(preset["chaine_signal"]))

    c.save()


def draw_dict_block(c, data, y, indent=60):
    c.setFont("Helvetica", 12)
    for key, value in data.items():
        y -= 20
        if isinstance(value, dict):
            c.drawString(indent, y, f"{key} :")
            y = draw_dict_block(c, value, y, indent + 20)
        else:
            c.drawString(indent, y, f"{key} : {value}")
    return y

import io

def generate_preset_pdf_flask(preset):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    y = height - 50
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, f"Preset : {preset['bassiste']}")

    y -= 30
    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Généré le : {datetime.now().strftime('%d/%m/%Y %H:%M')}")

    y -= 40
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Basse")
    y = draw_dict_block(c, preset["basse"], y)

    y -= 20
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Ampli")
    y = draw_dict_block(c, preset["ampli"], y)

    y -= 20
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Effets")
    for effet, reglages in preset["effets"].items():
        y -= 20
        c.setFont("Helvetica-Bold", 12)
        c.drawString(60, y, effet)
        y = draw_dict_block(c, reglages, y, indent=80)

    y -= 20
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Baffle")
    y = draw_dict_block(c, preset["baffle"], y)

    y -= 20
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Chaîne du signal")
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(60, y, " ➔ ".join(preset["chaine_signal"]))

    c.save()
    buffer.seek(0)
    return buffer


