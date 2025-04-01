
# base_bassistes.py

base_bassistes = {
    "Laurent Vernerey": {
        "cible_sonore": {
            "frequences_boost": [100, 250],
            "frequences_cut": [2500, 3000],
            "compression": {
                "type": "doux",
                "ratio": "4:1",
                "grain": "BUS"
            },
            "attaque": "moyenne",
            "caracteristiques": ["chaud", "rond", "dense"]
        },
        "description": "Son chaud et contrôlé, très équilibré dans le bas-médium, idéal pour les ballades ou les morceaux à forte présence émotionnelle."
    },

    "Jaco Pastorius": {
        "cible_sonore": {
            "frequences_boost": [800, 1200],
            "frequences_cut": [100, 60],
            "compression": {
                "type": "sec",
                "ratio": "3:1",
                "grain": "FET"
            },
            "attaque": "rapide",
            "caracteristiques": ["claquant", "nasal", "expressif"]
        },
        "description": "Son incisif et chantant, avec un médium très en avant et peu de grave. Typique des lignes fretless en solo ou en trio jazz fusion."
    }
}
