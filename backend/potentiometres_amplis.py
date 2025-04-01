"""
Dictionnaire associant chaque modèle d'ampli aux potentiomètres (réglages) disponibles.
Chaque clé est le nom de l'ampli, et la valeur est une liste de contrôles (chaînes).
"""

potentiometres_amplis = {
    "Aguilar DB 751": ["Gain", "Bass", "Midrange", "Treble", "Master Volume"],
    "Aguilar Tone Hammer 500": ["Gain", "Drive", "Bass", "Mid Level", "Mid Frequency", "Treble", "Master Volume"],
    "Ampeg B-15N": ["Volume", "Bass", "Treble"],
    "Ampeg Micro VR": ["Gain", "Bass", "Mid", "Treble", "Volume", "Limiter Switch"],
    "Ampeg PF-500": ["Gain", "Bass", "Midrange", "Frequency Selector", "Treble", "Volume", "Compressor"],
    "Ampeg SVT-2 Pro": ["Gain", "Bass", "Midrange", "Mid Selector", "Treble", "Graphic EQ", "Master Volume"],
    "Ampeg SVT-3 Pro": ["Gain", "Bass", "Midrange", "Mid Selector", "Treble", "Graphic EQ", "Master Volume"],
    "Ampeg SVT-4 Pro": ["Gain", "Bass", "Midrange", "Mid Selector", "Treble", "Graphic EQ", "Compressor", "Master Volume"],
    "Ampeg SVT-CL": ["Gain", "Bass", "Midrange", "Mid Selector", "Treble", "Master Volume", "Ultra Hi", "Ultra Lo"],
    "Ampeg SVT-VR": ["Volume 1", "Bass 1", "Treble 1", "Volume 2", "Bass 2", "Midrange 2", "Treble 2"],
    "Ampeg V-4B": ["Volume", "Bass", "Midrange", "Treble", "Ultra Hi", "Ultra Lo"],
    "Ashdown ABM 500 EVO IV": ["Input Level", "Bass", "Middle", "Treble", "Sub Harmonics", "Master Volume"],
    "Ashdown MAG 300": ["Input", "Bass", "Middle", "Treble", "Master"],
    "Ashdown Rootmaster RM-500": ["Input Level", "Bass", "Middle", "Treble", "Shape", "Master Volume"],
    "Chillamp Alpha": ["Gain", "Bass", "Mid", "Treble", "Présence", "Master Volume"],
    "Chillamp Bêta": ["Volume 1964", "Bass 1964", "Treble 1964", "Volume 1966", "Bass 1966", "Treble 1966", "Master Volume"],
    "Chillamp Delta": ["Gain", "Volume", "Bass", "Midrange", "Treble", "Présence", "Master"],
    "Darkglass Alpha-Omega 900": ["Gain", "Blend", "Level", "Drive", "Bass", "Mid", "Mid Frequency", "Treble", "Master Volume"],
    "Darkglass Microtubes 500": ["Gain", "Blend", "Level", "Drive", "Bass", "Mid", "Mid Frequency", "Treble", "Master Volume"],
    "Darkglass Microtubes 900 v2": ["Gain", "Blend", "Level", "Drive", "Bass", "Mid", "Mid Frequency", "Treble", "Master Volume"],
    "EBS HD360": ["Gain", "Compressor", "Bass", "Mid Frequency", "Mid Level", "Treble", "Bright", "Drive", "Volume"],
    "EBS Reidmar 750": ["Gain", "Bass", "Mid Freq", "Mid Level", "Treble", "Drive", "Volume"],
    "Eden WT800": ["Gain", "Enhance", "Bass", "Mid Sweep", "Mid Level", "Treble", "Master Volume"],
    "Fender Bassman 100T": ["Volume", "Bass", "Mid", "Treble", "Gain", "Master Volume"],
    "Fender Bassman 500": ["Volume", "Bass", "Mid", "Treble", "Gain", "Master Volume"],
    "Fender Rumble 100": ["Gain", "Bass", "Low Mid", "High Mid", "Treble", "Master Volume", "Overdrive", "Contour", "Vintage"],
    "Fender Rumble 200": ["Gain", "Bass", "Low Mid", "High Mid", "Treble", "Master Volume", "Overdrive", "Contour", "Vintage"],
    "Fender Rumble 500": ["Gain", "Bass", "Low Mid", "High Mid", "Treble", "Master Volume", "Overdrive", "Contour", "Vintage"],
    "Gallien-Krueger 1001RB": ["Gain", "Contour", "Presence", "Bass", "Low Mid", "High Mid", "Treble", "Boost", "Tweeter Level", "Woofer Level", "Master Volume"],
    "Gallien-Krueger 2001RB": ["Gain A", "Gain B", "Bass", "Low Mid", "High Mid", "Treble", "Boost A", "Boost B", "Tweeter Level", "Woofer Level", "Master Volume"],
    "Gallien-Krueger MB500": ["Gain", "Contour", "Bass", "Low Mid", "High Mid", "Treble", "Master Volume"],
    "Gallien-Krueger MB800": ["Gain", "Contour", "Bass", "Low Mid", "High Mid", "Treble", "Master Volume"],
    "Gallien-Krueger Fusion 550": ["Gain", "Tube Drive", "Bass", "Midrange", "Treble", "Contour", "Boost", "Master Volume"],
    "Genz-Benz Shuttle 6.2": ["Volume", "Gain", "Bass", "Midrange", "Mid Frequency", "Treble", "Master Volume"],
    "Genz-Benz Streamliner 600": ["Gain", "Volume", "Bass", "Mid", "Mid Frequency", "Treble", "Master Volume"],
    "Genz-Benz Streamliner STM-600": ["Gain", "Volume", "Bass", "Mid", "Mid Frequency", "Treble", "Master Volume"],
    "Glockenklang Blue Soul": ["Gain", "Bass", "Low Mid", "High Mid", "Treble", "Master Volume"],
    "Glockenklang Heart-Rock II": ["Gain", "Bass", "Low Mid", "High Mid", "Treble", "Master Volume"],
    "GR Bass One 800": ["Gain", "Bass", "Mid Low", "Mid High", "Treble", "Boost", "Master Volume"],
    "Hartke HA3500": ["Tube Level", "Solid State Level", "Bass", "Mid Band", "Mid Frequency", "Treble", "Compressor", "Master Volume"],
    "Hartke LH500": ["Volume", "Bass", "Midrange", "Treble", "Limiter"],
    "Hartke TX600": ["Drive", "Compressor", "Bass", "Midrange", "Treble", "Shape", "Master Volume"],
    "Markbass Little Mark II": ["Gain", "Bass", "Mid Low", "Mid High", "Treble", "VLE", "VPF", "Master Volume"],
    "Markbass Little Mark III": ["Gain", "Bass", "Mid Low", "Mid High", "Treble", "VLE", "VPF", "Master Volume"],
    "Markbass Little Mark Vintage": ["Gain", "Bass", "Mid Low", "Mid High", "Treble", "Drive", "VLE", "VPF", "Master Volume"],
    "Markbass TTE 500 Randy Jackson": ["Gain", "Colour", "Bass", "Midrange", "Treble", "Master Volume"],
    "Mesa Subway D-800": ["Input Level", "Voicing", "Bass", "Low Mid", "High Mid", "Treble", "Master Volume"],
    "Mesa Subway WD-800": ["Gain", "Bass", "Low Mid", "High Mid", "Treble", "Drive", "Voicing", "Master Volume"],
    "Mesa Boogie M6 Carbine": ["Gain", "Bass", "Midrange", "Treble", "Master Volume"],
    "Mesa Boogie M9 Carbine": ["Gain", "Bass", "Midrange", "Treble", "Graphic EQ", "Master Volume"],
    "Mesa Boogie Big Block 750": ["Gain", "Bass", "Midrange", "Treble", "Drive", "Master Volume"],
    "Orange AD200B MK3": ["Gain", "Bass", "Mid", "Treble", "Master Volume"],
    "Orange OB1-500": ["Gain Clean", "Gain Blend", "Blend", "Bass", "Midrange", "Treble", "Master Volume"],
    "Orange Terror Bass 500": ["Volume", "Bass", "Mid", "Treble", "Gain"],
    "Peavey Tour 700": ["Gain", "Bass", "Midrange", "Treble", "Contour", "Master Volume"],
    "Peavey Max 300": ["Gain", "Bass", "Midrange", "Treble", "Volume", "TransTube", "Contour"],
    "Phil Jones Bass BP-800": ["Input Level", "Bass", "Midrange", "Treble", "Master Volume"],
    "Quilter Bass Block 800": ["Gain", "Depth", "Contour", "Master Volume"],
    "TecAmp Puma 500": ["Gain", "Bass", "Low Mid", "High Mid", "Treble", "Taste", "Master Volume"],
    "Trace Elliot ELF": ["Gain", "Bass", "Mid", "Treble", "Volume"],
    "Trace Elliot AH600": ["Gain", "Bass", "Midrange", "Treble", "Master Volume"],
    "Traynor YBA200": ["Gain", "Bass", "Mid", "Treble", "Resonance", "Presence", "Master Volume"],
    "Trickfish Bullhead .5K": ["Gain", "Bass", "Low Mid", "High Mid", "Treble", "EQ Bypass", "Master Volume"],
    "Warwick LWA 1000": ["Gain A", "Gain B", "Bass A", "Bass B", "Mid A", "Mid B", "Treble A", "Treble B", "Master A", "Master B"]
}
