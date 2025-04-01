import sys
import os
# Ajouter la racine du dépôt au PYTHONPATH pour permettre l'import des modules situés à la racine
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, jsonify, send_file, send_from_directory
from preset_engine import get_presets_for_combination
from pdf_generator import generate_preset_pdf_flask
from bassistes import bassistes
from liste_basses_completes import basses_uniques
from liste_amplis_basse_complets import amplis_basse
from liste_effets_basse_complets import effets_basse
from liste_baffles_basse_complets import baffles_basse
from base_bassistes import base_bassistes

app = Flask(__name__)

# Endpoint pour générer un preset en JSON
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

# Endpoint pour générer un PDF du preset
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

# Endpoints pour renvoyer les listes de matériels
@app.route('/api/liste_basses', methods=["GET"])
def list_basses():
    return jsonify(basses_uniques)

@app.route('/api/liste_amplis', methods=["GET"])
def list_amplis():
    return jsonify(amplis_basse)

@app.route('/api/liste_effets', methods=["GET"])
def list_effets():
    return jsonify(effets_basse)

@app.route('/api/liste_baffles', methods=["GET"])
def list_baffles():
    return jsonify(baffles_basse)

@app.route('/api/liste_bassistes', methods=['GET'])
def list_bassistes():
    # Combine prénom et nom pour chaque bassiste
    names = [f"{b['prenom']} {b['nom']}" for b in bassistes]
    return jsonify(names)

# Endpoint pour servir la page d'accueil (index.html)
@app.route("/")
def index():
    return send_from_directory(os.path.join(os.path.dirname(__file__), "../frontend"), "index.html")

if __name__ == "__main__":
    # Récupère le port depuis la variable d'environnement PORT, sinon utilise 5000 par défaut
    port = int(os.environ.get("PORT", 5000))
    # Utilise la variable FLASK_DEBUG pour définir le mode debug (0 par défaut)
    debug_mode = os.environ.get("FLASK_DEBUG", "0") == "1"
    app.run(host="0.0.0.0", port=port, debug=debug_mode)
