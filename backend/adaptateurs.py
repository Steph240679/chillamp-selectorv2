# adaptateurs.py (version enrichie avec EQ actif adaptatif)

from potentiometres_amplis import potentiometres_amplis
from basses_avec_type import basses_avec_type


def adapter_basse(basse, cible):
    caractere = cible.get("caractere", "")
    tone = 70
    volume = 100

    if "chaud" in caractere:
        tone = 60
    elif "claquant" in caractere:
        tone = 80

    mic_position = "default"
    if "rondeur" in caractere:
        mic_position = "neck only"
    elif "attaque" in caractere or "growl" in caractere or "punch" in caractere:
        mic_position = "both"
    elif "claquant" in caractere:
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
        if "chaud" in caractere or "rond" in caractere:
            eq_actif["Bass"] += 10
            eq_actif["Treble"] -= 10
        if "claquant" in caractere:
            eq_actif["Treble"] += 10
        if "attaque" in caractere or "growl" in caractere:
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
    reglages = {}

    for potard in potards:
        potard_lc = potard.lower()
        if "bass" in potard_lc:
            reglages[potard] = 70 if "chaud" in caractere else 60
        elif "mid" in potard_lc:
            reglages[potard] = 50 if "scooped" in caractere else 65
        elif "treble" in potard_lc:
            reglages[potard] = 60 if "claquant" in caractere else 50
        elif "gain" in potard_lc:
            reglages[potard] = 55
        elif "volume" in potard_lc or "master" in potard_lc:
            reglages[potard] = 80
        elif "presence" in potard_lc:
            reglages[potard] = 60 if "vintage" in caractere else 70
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
