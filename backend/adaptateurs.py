from potentiometres_amplis import potentiometres_amplis

def adapter_basse(basse, cible):
    """
    Adapte les réglages de la basse en fonction du modèle et du profil cible.
    """
    caractere = cible.get("caractere", "")
    tone = 70
    if "chaud" in caractere:
        tone = 60
    elif "claquant" in caractere:
        tone = 80

    mic_position = "default"
    if "rondeur" in caractere:
        mic_position = "neck only"
    elif "attaque" in caractere:
        mic_position = "bridge only"
        if "attaque" in caractere or "growl" in caractere or "punch" in caractere:
    mic_position = "both"

    return {
        "volume": 100,
        "tone": tone,
        "mic_position": mic_position
    }

def adapter_ampli(ampli, cible):
    """
    Adapte les réglages de l'ampli selon le profil cible.
    """
    potards = potentiometres_amplis.get(ampli, [])
    caractere = cible.get("caractere", "")
    reglages = {}
    
    for potard in potards:
        potard_lc = potard.lower()
        if "bass" in potard_lc:
            reglages[potard] = 70 if "chaud" in caractere else 60
        elif "mid" in potard_lc:
            reglages[potard] = 50 if "scooped" in caractere else 65
            if "mid" in potard_lc:
    reglages[potard] = 65 + ajustement_baffle
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
    """
    Adapte les réglages pour les effets en fonction du profil cible.
    """
    effets_reglages = {}
    for effet in effets_utilisateur:
        if effet in cible.get("reglages_effets", {}):
            effets_reglages[effet] = cible["reglages_effets"][effet]
        else:
            effets_reglages[effet] = {"niveau": 50, "reglage": "par défaut"}
    return effets_reglages

def adapter_baffle(baffle, cible):
    """
    Adapte le profil du baffle en fonction du modèle et du profil cible.
    """
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
    """
    Génère la chaîne du signal en concaténant les noms des composants.
    """
    return [basse] + effets + [ampli, baffle]
