from flask import Flask, request, jsonify, send_file, send_from_directory
import os
from preset_engine import get_presets_for_combination
from pdf_generator import generate_preset_pdf_flask

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
    # Assure-toi que le dossier 'frontend' est à la racine du dépôt
    return send_from_directory(os.path.join(os.path.dirname(__file__), "../frontend"), "index.html")

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
  
