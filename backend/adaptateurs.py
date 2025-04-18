from potentiometres_amplis import potentiometres_amplis
from basses_avec_type import basses_avec_type


def adapter_basse(basse, cible):
    caractere = cible.get("caractere", "")
    mot_cle = caractere.split()[-1].lower()  # extrait le mot-clé final

    tone = 70
    volume = 100

    if mot_cle == "chaud":
        tone = 60
    elif mot_cle == "claquant":
        tone = 80

    mic_position = "default"
    if mot_cle == "rondeur":
        mic_position = "neck only"
    elif mot_cle in ["attaque", "growl", "punch"]:
        mic_position = "both"
    elif mot_cle == "claquant":
        mic_position = "bridge only"

    type_basse = basses_avec_type.get(basse, "passive")
    eq_actif = None

    if type_basse == "active":
        volume = 90
        eq_actif = {
            "Bass": 60,
            "Medium": 60,
            "Treble": 60
        }
        if mot_cle in ["chaud", "rond"]:
            eq_actif["Bass"] += 10
            eq_actif["Treble"] -= 10
        if mot_cle == "claquant":
            eq_actif["Treble"] += 10
        if mot_cle in ["attaque", "growl", "punch"]:
            eq_actif["Medium"] += 10

    resultat = {
        "volume": volume,
        "tone": tone,
        "mic_position": mic_position
    }

    if eq_actif:
        resultat["EQ actif"] = eq_actif

    return resultat


def adapter_ampli(ampli, cible):
    potards = potentiometres_amplis.get(ampli, [])
    caractere = cible.get("caractere", "")
    mot_cle = caractere.split()[-1].lower()

    reglages = {}

    for potard in potards:
        potard_lc = potard.lower()
        if "bass" in potard_lc:
            reglages[potard] = 70 if mot_cle == "chaud" else 60
        elif "mid" in potard_lc:
            reglages[potard] = 50 if mot_cle == "scooped" else 65
        elif "treble" in potard_lc:
            reglages[potard] = 60 if mot_cle == "claquant" else 50
        elif "gain" in potard_lc:
            reglages[potard] = 55
        elif "volume" in potard_lc or "master" in potard_lc:
            reglages[potard] = 80
        elif "presence" in potard_lc:
            reglages[potard] = 60 if mot_cle == "vintage" else 70
        else:
            reglages[potard] = 50

    return reglages


def adapter_effets(effets_utilisateur, cible):
    effets_reglages = {}
    for effet in effets_utilisateur:
        if effet in cible.get("reglages_effets", {}):
            effets_reglages[effet] = cible["reglages_effets"][effet]
        else:
            effets_reglages[effet] = {"niveau": 50, "reglage": "par défaut"}
    return effets_reglages


def adapter_baffle(baffle, cible):
    caractere = "neutre"
    ajustement = 0

    if "1x10" in baffle:
        caractere = "compact"
        ajustement = -3
    elif "2x10" in baffle:
        caractere = "rapide et défini"
        ajustement = -2
    elif "1x12" in baffle:
        caractere = "polyvalent"
        ajustement = 0
    elif "2x12" in baffle:
        caractere = "équilibré et punchy"
        ajustement = +2
    elif "4x10" in baffle:
        caractere = "percutant"
        ajustement = -5
    elif "1x15" in baffle:
        caractere = "rond"
        ajustement = +5
    elif "4x12" in baffle:
        caractere = "médium prononcé"
        ajustement = +3
    elif "8x10" in baffle:
        caractere = "massif et direct"
        ajustement = +6

    return {
        "caractere": caractere,
        "ajustement": ajustement
    }


def generer_chaine_signal(basse, effets, ampli, baffle):
    return [basse] + effets + [ampli, baffle]
