# preset_engine.py

from base_bassistes import base_bassistes
from adaptateurs import (
    adapter_basse,
    adapter_ampli,
    adapter_effets,
    adapter_baffle,
    generer_chaine_signal
)

def get_presets_for_combination(bassiste, basse, ampli, effets, baffle):
    cible = base_bassistes[bassiste]

    reglage_basse = adapter_basse(basse, cible)
    reglage_ampli = adapter_ampli(ampli, cible)
    reglage_effets = adapter_effets(effets, cible)
    reglage_baffle = adapter_baffle(baffle, cible)

    chaine_signal = generer_chaine_signal(basse, effets, ampli, baffle)

    return {
        "bassiste": bassiste,
        "basse": {
            "modele": basse,
            "reglages": reglage_basse
        },
        "ampli": {
            "modele": ampli,
            "reglages": reglage_ampli
        },
        "effets": reglage_effets,
        "baffle": {
            "modele": baffle,
            "profil": reglage_baffle
        },
        "chaine_signal": chaine_signal
    }
