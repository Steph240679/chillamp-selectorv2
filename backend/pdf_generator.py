from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
import io

def _draw_preset_content(c, preset):
    """
    Dessine le contenu du preset sur le canvas ReportLab.
    """
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
    for effet in preset["effets"]:
        nom_effet = effet.get("nom", "Effet inconnu")
        reglages = effet.get("reglages", {})

        y -= 20
        c.setFont("Helvetica-Bold", 12)
        c.drawString(60, y, nom_effet)

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

    return c

def draw_dict_block(c, data, y, indent=60):
    """
    Dessine un bloc de texte pour un dictionnaire sur le canvas.
    """
    c.setFont("Helvetica", 12)
    for key, value in data.items():
        y -= 20
        if isinstance(value, dict):
            c.drawString(indent, y, f"{key} :")
            y = draw_dict_block(c, value, y, indent + 20)
        else:
            c.drawString(indent, y, f"{key} : {value}")
    return y

def generate_preset_pdf(preset, filename="preset.pdf"):
    """
    Génère un PDF à partir d'un preset et l'enregistre sur disque.
    """
    c = canvas.Canvas(filename, pagesize=A4)
    _draw_preset_content(c, preset)
    c.save()

def generate_preset_pdf_flask(preset):
    """
    Génère un PDF à partir d'un preset et retourne un buffer pour Flask.
    """
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    _draw_preset_content(c, preset)
    c.save()
    buffer.seek(0)
    return buffer
