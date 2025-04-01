"""
Base des profils de bassistes pour adapter les presets.
Chaque entrée associe le nom du bassiste à un dictionnaire contenant au moins :
- "caractere": description sommaire du son cible
- "reglages_effets": réglages par défaut pour les effets (modifiable selon besoin)
"""

base_bassistes = {
    "Michel Alibo": {"caractere": "fluide, chantant, doux", "reglages_effets": {}},
    "Manu Baroux": {"caractere": "chaud, rond, ample", "reglages_effets": {}},
    "Nick Beggs": {"caractere": "synthétique, expressif", "reglages_effets": {}},
    "Michaël Benjelloun": {"caractere": "discret, précis", "reglages_effets": {}},
    "Franck Biyong": {"caractere": "énergique, nerveux", "reglages_effets": {}},
    "Jean Bisello": {"caractere": "souple, droit", "reglages_effets": {}},
    "Tim Bogert": {"caractere": "gras, agressif", "reglages_effets": {}},
    "Richard Bona": {"caractere": "lyrique, chantant", "reglages_effets": {}},
    "Bunny Brunel": {"caractere": "ultra défini, articulé", "reglages_effets": {}},
    "Jack Bruce": {"caractere": "crémeux, saturé", "reglages_effets": {}}
    # Ajoute d'autres profils selon les besoins
}
