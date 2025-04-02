import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, jsonify, send_file, send_from_directory
from preset_engine import get_presets_for_combination
from pdf_generator import generate_preset_pdf_flask
from bassistes import bassistes
from basses_avec_type import basses_avec_type
from liste_amplis_basse_complets import amplis_basse
from liste_effets_basse_complets import effets_basse
from liste_baffles_basse_complets import baffles_basse
from base_bassistes import base_bassistes

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
    preset["basse"]["type"] = basses_avec_type.get(basse, "passive")
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
    preset["basse"]["type"] = basses_avec_type.get(basse, "passive")

    pdf_buffer = generate_preset_pdf_flask(preset)
    return send_file(
        pdf_buffer,
        as_attachment=True,
        download_name="preset_chillamp.pdf",
        mimetype="application/pdf"
    )

@app.route('/api/liste_basses', methods=["GET"])
def list_basses():
    # On retourne les noms de basses triés
    return jsonify(sorted(basses_avec_type.keys()))

@app.route('/api/liste_amplis', methods=["GET"])
def list_amplis():
    return jsonify(amplis_basse)

@app.route('/api/liste_effets', methods=["GET"])
def list_effets():
    return jsonify(effets_basse)

@app.route('/api/liste_baffles', methods=["GET"])
def list_baffles():
    # On retourne les baffles triés par ordre alphabétique
    return jsonify(sorted(baffles_basse))

@app.route('/api/liste_bassistes', methods=['GET'])
def list_bassistes():
    # On retourne la liste complète des bassistes, triée par la clé de correspondance
    sorted_bassistes = sorted(bassistes, key=lambda b: b["cle"])
    return jsonify(sorted_bassistes)

@app.route("/")
def index():
    # Envoi du fichier index.html depuis le dossier frontend
    return send_from_directory(os.path.join(os.path.dirname(__file__), "../frontend"), "index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug_mode = os.environ.get("FLASK_DEBUG", "0") == "1"
    app.run(host="0.0.0.0", port=port, debug=debug_mode)
