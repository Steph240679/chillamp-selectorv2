"""
Dictionnaire associant à chaque bassiste une description du son ciblé.

Chaque entrée décrit le caractère sonore typique du musicien, servant à orienter
les réglages dans la génération des presets.
"""

sons_cibles = {
    "Michel Alibo": "Son fluide et chantant, très mélodique avec une attaque douce, idéal pour la fusion jazz et les musiques caribéennes.",
    "Manu Baroux": "Son chaud et rond, typé soul/funk, avec un groove régulier et ample.",
    "Nick Beggs": "Son synthétique et expressif, souvent avec des effets, typique du rock progressif moderne.",
    "Michaël Benjelloun": "Son discret et précis, adapté à la chanson française et au travail de studio.",
    "Franck Biyong": "Son énergique et nerveux, mêlant afrobeat, rock et textures saturées.",
    "Jean Bisello": "Son souple et droit, efficace pour le jazz et les formations acoustiques.",
    "Tim Bogert": "Son gras et agressif, avec beaucoup de saturation et de présence dans les médiums.",
    "Richard Bona": "Son lyrique, très chantant, avec des aigus soyeux et un médium expressif.",
    "Bunny Brunel": "Son ultra défini, articulé, typique du jazz fusion à très haute précision.",
    "Jack Bruce": "Son crémeux et saturé, très expressif, ancré dans le rock psychédélique et bluesy.",
    "Philippe Bussonnet": "Son massif et riche, puissant dans les bas-médiums, avec une grande dynamique pour le jazz-rock.",
    "Laurent Cokelaere": "Son percutant, efficace, bien présent dans le mix rock français.",
    "Adam Clayton": "Son simple et efficace, souvent enveloppé d’effets pour une assise stable chez U2.",
    "Stanley Clarke": "Son virtuose, claquant, avec une large palette dynamique, souvent en slap.",
    "Bootsy Collins": "Son funky, saturé et groovy, avec une personnalité sonore exubérante.",
    "Tim Commerford": "Son massif et compressé, très en avant, avec distorsion contrôlée.",
    "Victoria De Angelis": "Son nerveux et rugueux, très rock garage avec une attaque franche.",
    "John Deacon": "Son chaud, discret et mélodique, parfaitement intégré dans les compositions.",
    "Kim Deal": "Son minimaliste et brut, au service de l’énergie et du groove lo-fi.",
    "Mike Dirnt": "Son précis et rapide, très défini pour supporter le punk rock.",
    "Gail Ann Dorsey": "Son profond et moelleux, avec une belle articulation et rondeur.",
    "Fred Dupont": "Son massif et tendu, très adapté au rock alternatif français.",
    "Nathan East": "Son très propre, équilibré, adapté à tous les styles, studio par excellence.",
    "John Entwistle": "Son ultra articulé, presque lead, avec une grande rapidité et densité sonore.",
    "Hadrien Feraud": "Son brillant et complexe, typé jazz fusion moderne, très technique.",
    "Nicolas Fiszman": "Son polyvalent, à l'aise dans tous les styles, toujours bien placé.",
    "Norwood Fisher": "Son funky et audacieux, souvent saturé avec un sens de la provocation sonore.",
    "Flea": "Son explosif, très dynamique, avec slap puissant et médiums claquants.",
    "Roger Glover": "Son chaud et bien appuyé dans le mix, avec une basse rock stable.",
    "Mike Gordon": "Son organique et moelleux, très souple pour le jam-band.",
    "Steve Harris": "Son très rapide, claquant et tranchant, au médiator dans les aigus.",
    "Jonas Hellborg": "Son ample et texturé, très libre dans les médiums et les dynamiques.",
    "Mark Hoppus": "Son pop-punk équilibré, efficace, avec beaucoup de soutien.",
    "Peter Hook": "Son médium aigu très mélodique, souvent en rôle de guitare basse lead.",
    "Sean Hurley": "Son propre et subtil, parfait pour la pop rock et les sessions studio.",
    "James Jamerson": "Son rond, coulant, syncopé, très expressif pour le Motown classique.",
    "Darryl Jones": "Son moderne, très stable, ancré et profond, idéal en live.",
    "Jean-Michel Kajdan": "Son clair, précis, souvent mélodique, avec influence jazz.",
    "Tony Kanal": "Son brillant et punchy, parfait pour le ska et le rock pop.",
    "Carol Kaye": "Son sec, défini, toujours très propre, typique des studios 60s–70s.",
    "Lemmy Kilmister": "Son saturé, rugueux et très agressif, un mur sonore à lui seul.",
    "Bakithi Kumalo": "Son fretless chantant, très rapide et fluide, avec des influences africaines.",
    "Romain Labaye": "Son précis, moderne et souple, très défini dans le registre grave.",
    "Geddy Lee": "Son médium claquant, très articulé, avec une signature reconnaissable.",
    "Will Lee": "Son polyvalent, studio, précis et musical, toujours adapté au contexte.",
    "Phil Lesh": "Son libre, improvisé, organique, idéal pour les jams longs et aérés.",
    "Tony Levin": "Son profond, texturé, souvent expérimental avec le Chapman Stick.",
    "Phil Lynott": "Son chaud et simple, souvent en soutien des lignes vocales.",
    "Graham Maby": "Son mélodique et élégant, parfaitement intégré aux arrangements.",
    "Michael Manring": "Son poétique, très ambiant, avec usage de microtonalités et fretless.",
    "Etienne Mbappé": "Son velouté, très chantant, avec une touche africaine subtile.",
    "Paul McCartney": "Son mélodique, chantant, toujours au service de la chanson.",
    "John McVie": "Son solide et discret, très ancré dans le groove de Fleetwood Mac.",
    "Nate Mendel": "Son épais, simple et efficace, parfait pour le rock US moderne.",
    "Martin Mendez": "Son sombre, puissant et articulé, au service du metal progressif.",
    "Jocelyn Mienniel": "Son électro-acoustique, texturé, très expérimental.",
    "Marcus Miller": "Son claquant, slappé, très net et articulé, signature jazz funk.",
    "Jean-Philippe Morel": "Son contemporain, sobre, au service du collectif jazz.",
    "Louis Moutin": "Son jazz vif et organique, entre contrebasse et électrique.",
    "Pascal Mulot": "Son très tranchant, rapide et technique, pour le metal et le shred.",
    "John Myung": "Son précis, rapide, très compressé, pour les architectures prog.",
    "Meshell Ndegeocello": "Son profond, introspectif, très texturé, souvent influencé par la soul.",
    "Jason Newsted": "Son agressif, au médiator, parfaitement taillé pour le thrash metal.",
    "Bernard Paganotti": "Son lourd et structuré, typé zeuhl/jazz-rock français.",
    "Pino Palladino": "Son rond, souple et expressif, en fingerstyle ou fretless.",
    "Jaco Pastorius": "Son légendaire fretless, chantant, médiums expressifs et harmoniques.",
    "Rocco Prestia": "Son staccato hyper précis, funky, rythmique et sec.",
    "Dee Dee Ramone": "Son brut et rapide, ultra minimaliste pour le punk.",
    "Stéphan Rossi": "Son équilibré et pro, très adapté à la variété et au studio.",
    "Alexis Rostand": "Son dansant et funky, moderne et pop à la française.",
    "Mike Rutherford": "Son progressif discret, toujours efficace dans le groove.",
    "Armand Sabal-Lecco": "Son puissant, chaud et fluide, avec beaucoup de nuances africaines.",
    "Leland Sklar": "Son doux, rond, ultra propre, typique du studio US.",
    "Esperanza Spalding": "Son jazz expressif, très lyrique, en finger ou en contrebasse.",
    "Chris Squire": "Son brillant et agressif, très en avant dans le mix prog rock.",
    "John Taylor": "Son funky et dansant, très 80s et synthétique.",
    "Henri Texier": "Son jazz profond, aux résonances boisées, souvent à la contrebasse.",
    "Laurent Vernerey": "Son chaud, précis, grave bien tenu, très propre en studio live.",
    "Roger Waters": "Son simple, droit et grave, servant la narration musicale.",
    "Tina Weymouth": "Son new wave minimaliste et rebondissant, très rythmique.",
    "Tal Wilkenfeld": "Son doux mais expressif, très sensible et technique.",
    "Doug Wimbish": "Son saturé, texturé, très créatif, entre rock, hip-hop et métal.",
    "Victor Wooten": "Son ultra technique, slappé, inventif, avec une grande musicalité.",
    "Jennifer Young": "Son fluide et rapide, très propre, dans un contexte rock instrumental."
}
