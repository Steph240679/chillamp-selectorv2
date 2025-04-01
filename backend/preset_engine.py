
# preset_engine.py

from base_bassistes import base_bassistes

def get_presets_for_combination(bassiste, basse, ampli, effets, baffle):
    cible = base_bassistes[bassiste]["cible_sonore"]
    reglage_basse = adapter_basse(basse, cible)
    reglage_ampli = adapter_ampli(ampli, cible)
    reglage_effets = adapter_effets(effets, cible)
    reglage_baffle = adapter_baffle(baffle, cible)

    chaine_signal = generer_chaine_signal(basse, effets, ampli, baffle)

    return {
        "bassiste": bassiste,
        "basse": reglage_basse,
        "ampli": reglage_ampli,
        "effets": reglage_effets,
        "baffle": reglage_baffle,
        "chaine_signal": chaine_signal
    }

def adapter_basse(nom_basse, cible):
    if "Sterling" in nom_basse:
        return {
            "mode": "série",
            "EQ onboard": {
                "bass": "+25%",
                "mid": "+40%",
                "treble": "-30%"
            },
            "tone": "n/a"
        }
    elif "Precision" in nom_basse:
        return {"tone": "30–40%", "volume": "100%"}
    else:
        return {
            "EQ onboard": {
                "bass": "+15%" if 100 in cible["frequences_boost"] else "0%",
                "mid": "+10%" if 250 in cible["frequences_boost"] else "0%",
                "treble": "-20%" if any(f >= 2500 for f in cible["frequences_cut"]) else "0%"
            }
        }

def adapter_ampli(nom_ampli, cible):
    if "Streamliner" in nom_ampli:
        return {
            "gain": "11h",
            "bass": "13h",
            "mid": "14h",
            "mid_freq": "600 Hz",
            "treble": "10h"
        }
    elif "Delta" in nom_ampli:
        return {
            "gain": "11h",
            "bass": "13h",
            "middle": "14h",
            "treble": "10h",
            "presence": "10h"
        }
    else:
        return {
            "bass": "13h" if 100 in cible["frequences_boost"] else "12h",
            "mid": "14h" if 250 in cible["frequences_boost"] else "12h",
            "treble": "10h" if any(f >= 2500 for f in cible["frequences_cut"]) else "12h"
        }

def adapter_effets(effets, cible):
    result = {}
    for effet in effets:
        if effet == "Hyper Luminal":
            result["Hyper Luminal"] = {
                "mode": cible["compression"]["grain"],
                "blend": 65,
                "time": 40,
                "output": 65,
                "ratio": cible["compression"]["ratio"]
            }
        elif effet == "Empress Para EQ":
            result["Empress Para EQ"] = {
                "low_gain": 6 if 100 in cible["frequences_boost"] else 0,
                "low_freq": 100,
                "mid_gain": 6 if 250 in cible["frequences_boost"] else 0,
                "mid_freq": 250,
                "high_gain": -4 if any(f >= 2500 for f in cible["frequences_cut"]) else 0,
                "high_freq": 3000
            }
        elif effet == "Boss Delay":
            result["Boss Delay"] = {
                "mode": "analog",
                "time": "300 ms",
                "feedback": 2,
                "level": "15%"
            }
    return result

def adapter_baffle(nom_baffle, cible):
    if "Neo 1x10" in nom_baffle:
        return {"positionnement": "surélevé", "compensation_grave": True}
    elif "Classic 4x12" in nom_baffle:
        return {"nature": "clos", "projection": "forte"}
    else:
        return {"nature": "standard", "remarque": "adapter EQ en fonction"}

def generer_chaine_signal(basse, effets, ampli, baffle):
    return [basse] + sorted(effets) + [ampli, baffle]
