# app.py (Flask API pour chillamp-selector)

from flask import Flask, request, jsonify
from preset_engine import get_presets_for_combination

app = Flask(__name__)

@app.route("/api/preset", methods=["POST"])
def generate_preset():
    data = request.get_json()

    bassiste = data.get("bassiste")
    basse = data.get("basse")
    ampli = data.get("ampli")
    effets = data.get("effets", [])
    baffle = data.get("baffle")

    preset = get_presets_for_combination(bassiste, basse, ampli, effets, baffle)
    return jsonify(preset)

if __name__ == "__main__":
    app.run(debug=True)

from flask import send_file
from pdf_generator import generate_preset_pdf_flask

@app.route("/api/preset/pdf", methods=["POST"])
def generate_preset_pdf():
    data = request.get_json()
    bassiste = data.get("bassiste")
    basse = data.get("basse")
    ampli = data.get("ampli")
    effets = data.get("effets", [])
    baffle = data.get("baffle")

    preset = get_presets_for_combination(bassiste, basse, ampli, effets, baffle)
    pdf_buffer = generate_preset_pdf_flask(preset)
    return send_file(pdf_buffer, as_attachment=True, download_name="preset_chillamp.pdf", mimetype="application/pdf")

from flask import send_from_directory
import os

@app.route("/")
def index():
    return send_from_directory(os.path.join(os.path.dirname(__file__), "../frontend"), "index.html")


