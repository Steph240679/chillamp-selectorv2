# effets_details.py

effets_details = {
    "Compressor (Darkglass Hyper Luminal)": {
        "description": "Compresseur hybride à modélisation analogique (BUS, FET, SYM) avec un blend transparent",
        "controls": {
            "Blend": {
                "type": "potard",
                "plage": "0% – 100%",
                "effet": "Mélange du signal compressé avec le signal direct"
            },
            "Time": {
                "type": "potard",
                "plage": "0 – 100%",
                "effet": "Réglage combiné du temps d’attaque et de relâchement"
            },
            "Output": {
                "type": "potard",
                "plage": "-∞ à +20 dB",
                "effet": "Volume de sortie général"
            },
            "Ratio": {
                "type": "potard",
                "plage": "1:1 à ∞:1",
                "effet": "Taux de compression"
            },
            "Mode": {
                "type": "switch",
                "options": ["BUS", "FET", "SYM"],
                "effet": "Style de compression modélisé"
            }
        }
    },
    "Parametric EQ (Empress ParaEQ)": {
        "description": "EQ paramétrique 3 bandes ultra transparent avec boost intégré",
        "controls": {
            "Low Gain": {
                "type": "potard",
                "plage": "-15 dB à +15 dB",
                "effet": "Gain des basses"
            },
            "Low Frequency": {
                "type": "potard",
                "plage": "35 Hz – 500 Hz",
                "effet": "Fréquence ciblée pour les basses"
            },
            "Mid Gain": {
                "type": "potard",
                "plage": "-15 dB à +15 dB",
                "effet": "Gain des médiums"
            },
            "Mid Frequency": {
                "type": "potard",
                "plage": "250 Hz – 5 kHz",
                "effet": "Fréquence ciblée pour les médiums"
            },
            "Q": {
                "type": "potard",
                "plage": "Narrow à Wide",
                "effet": "Largeur de bande pour les médiums"
            },
            "High Gain": {
                "type": "potard",
                "plage": "-15 dB à +15 dB",
                "effet": "Gain des aigus"
            },
            "Boost Switch": {
                "type": "switch",
                "options": ["Off", "On"],
                "effet": "Ajout d’un boost global de +30 dB"
            }
        }
    },
    "Bass Preamp (Aguilar Tone Hammer)": {
        "description": "Préampli avec overdrive douce et EQ 3 bandes active + contour",
        "controls": {
            "Gain": {
                "type": "potard",
                "plage": "0 – 100%",
                "effet": "Ajoute du drive et augmente le niveau d’entrée"
            },
            "Bass": {
                "type": "potard",
                "plage": "-18 dB à +18 dB",
                "effet": "Égalisation des basses"
            },
            "Mid Level": {
                "type": "potard",
                "plage": "-16 dB à +16 dB",
                "effet": "Gain des médiums"
            },
            "Mid Frequency": {
                "type": "potard",
                "plage": "180 Hz – 1 kHz",
                "effet": "Fréquence ciblée des médiums"
            },
            "Treble": {
                "type": "potard",
                "plage": "-16 dB à +16 dB",
                "effet": "Égalisation des aigus"
            },
            "Master": {
                "type": "potard",
                "plage": "0 – 100%",
                "effet": "Volume de sortie général"
            }
        }
    },
    "Bass Distortion (Darkglass Microtubes B3K)": {
        "description": "Distorsion moderne très dynamique avec blend et contrôle des hautes fréquences",
        "controls": {
            "Blend": {
                "type": "potard",
                "plage": "0% – 100%",
                "effet": "Mix entre clean et disto"
            },
            "Level": {
                "type": "potard",
                "plage": "0 – 100%",
                "effet": "Volume de sortie"
            },
            "Drive": {
                "type": "potard",
                "plage": "0 – 100%",
                "effet": "Quantité de gain appliquée"
            },
            "Grunt Switch": {
                "type": "switch",
                "options": ["Thin", "Fat", "Raw"],
                "effet": "Réponse des basses"
            },
            "Attack Switch": {
                "type": "switch",
                "options": ["Flat", "Boost"],
                "effet": "Brillance et définition des attaques"
            }
        }
    },
    "Bass Chorus (Boss CEB-3)": {
        "description": "Chorus stéréo conçu pour basse, avec filtre de fréquence grave",
        "controls": {
            "Effect Level": {
                "type": "potard",
                "plage": "0 – 10",
                "effet": "Quantité de signal traité dans le mix"
            },
            "Low Filter": {
                "type": "potard",
                "plage": "20 Hz – 1.5 kHz",
                "effet": "Plage de fréquences affectée"
            },
            "Rate": {
                "type": "potard",
                "plage": "0 – 10",
                "effet": "Vitesse du modulateur"
            },
            "Depth": {
                "type": "potard",
                "plage": "0 – 10",
                "effet": "Profondeur du chorus"
            }
        }
    },
    "Envelope Filter (Electro-Harmonix Q-Tron)": {
        "description": "Auto-wah funky avec attaque dynamique et filtre sélectionnable",
        "controls": {
            "Drive": {
                "type": "potard",
                "plage": "0 – 10",
                "effet": "Sensibilité à l’attaque du jeu"
            },
            "Q": {
                "type": "potard",
                "plage": "0 – 10",
                "effet": "Accentuation de la résonance"
            },
            "Mode": {
                "type": "switch",
                "options": ["LP", "BP", "HP"],
                "effet": "Type de filtre : passe-bas, passe-bande, passe-haut"
            },
            "Range": {
                "type": "switch",
                "options": ["Lo", "Hi"],
                "effet": "Plage dynamique du filtre"
            }
        }
    },
    "Bass Octaver (EBS OctaBass)": {
        "description": "Octaver analogique qui suit bien le jeu rapide avec 3 modes de tracking",
        "controls": {
            "Normal": {
                "type": "potard",
                "plage": "0 – 100%",
                "effet": "Volume du signal original"
            },
            "Octave": {
                "type": "potard",
                "plage": "0 – 100%",
                "effet": "Volume de l’octave inférieure"
            },
            "Range": {
                "type": "switch",
                "options": ["High", "Mid", "Low"],
                "effet": "Tracking en fonction de la fréquence du jeu"
            }
        }
    },
    "Bass Fuzz (Way Huge Pork Loin)": {
        "description": "Fuzz chaud et musical avec clean blend et tone shaping interne",
        "controls": {
            "Volume": {
                "type": "potard",
                "plage": "0 – 100%",
                "effet": "Volume de sortie"
            },
            "Tone": {
                "type": "potard",
                "plage": "Dark – Bright",
                "effet": "Équilibre tonal"
            },
            "Overdrive": {
                "type": "potard",
                "plage": "0 – 100%",
                "effet": "Quantité de saturation"
            },
            "Clean": {
                "type": "potard",
                "plage": "0 – 100%",
                "effet": "Niveau du signal clean"
            }
        }
    },
    "Multi Band Compressor (tc electronic SpectraComp)": {
        "description": "Compresseur multibande très simple d'utilisation avec réglage unique",
        "controls": {
            "Comp": {
                "type": "potard",
                "plage": "0 – 100%",
                "effet": "Intensité de la compression sur toutes les bandes"
            }
        }
    },
    "Drive + EQ (Aguilar Agro)": {
        "description": "Overdrive mordante et musicale avec égalisation intégrée",
        "controls": {
            "Level": {
                "type": "potard",
                "plage": "0 – 100%",
                "effet": "Volume global"
            },
            "Saturation": {
                "type": "potard",
                "plage": "0 – 100%",
                "effet": "Quantité de drive"
            },
            "Contour": {
                "type": "potard",
                "plage": "0 – 100%",
                "effet": "Sculpte les médiums (scoop progressif)"
            },
            "Presence": {
                "type": "potard",
                "plage": "0 – 100%",
                "effet": "Accentue les hautes fréquences"
            }
        }
    }
}
