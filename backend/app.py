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
