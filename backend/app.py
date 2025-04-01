import os
from flask import Flask, request, jsonify, send_file, send_from_directory
from preset_engine import get_presets_for_combination
from pdf_generator import generate_preset_pdf_flask
from bassistes import bassistes
from liste_basses_completes import basses_uniques
from liste_amplis_basse_complets import amplis_basse
from liste_effets_basse_complets import effets_basse
from liste_baffles_basse_complets import baffles_basse

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

@app.route("/")
def index():
    return send_from_directory(os.path.join(os.path.dirname(__file__), "../frontend"), "index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    # On considère le mode production par défaut en déploiement
    debug_mode = os.environ.get("FLASK_ENV", "production") != "production"
    app.run(host="0.0.0.0", port=port, debug=debug_mode)
