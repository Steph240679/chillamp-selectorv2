# bassistes.py — Liste complète avec nom, prénom, groupe, clé de correspondance (doublons filtrés et triés)

bassistes = [
    {"nom": "Alibo", "prenom": "Michel", "groupe": "Sixun, Studio France", "cle": "Alibo Michel"},
    {"nom": "Baroux", "prenom": "Manu", "groupe": "Studio France", "cle": "Baroux Manu"},
    {"nom": "Beggs", "prenom": "Nick", "groupe": "Steven Wilson", "cle": "Beggs Nick"},
    {"nom": "Benjelloun", "prenom": "Michaël", "groupe": "Studio", "cle": "Benjelloun Michaël"},
    {"nom": "Biyong", "prenom": "Franck", "groupe": "Afrobeat Fusion", "cle": "Biyong Franck"},
    {"nom": "Bisello", "prenom": "Jean", "groupe": "Jazz", "cle": "Bisello Jean"},
    {"nom": "Bogert", "prenom": "Tim", "groupe": "Vanilla Fudge", "cle": "Bogert Tim"},
    {"nom": "Bona", "prenom": "Richard", "groupe": "Solo, Pat Metheny", "cle": "Bona Richard"},
    {"nom": "Bruce", "prenom": "Jack", "groupe": "Cream", "cle": "Bruce Jack"},
    {"nom": "Bussonnet", "prenom": "Philippe", "groupe": "Magma", "cle": "Bussonnet Philippe"},
    {"nom": "Clayton", "prenom": "Adam", "groupe": "U2", "cle": "Clayton Adam"},
    {"nom": "Collins", "prenom": "Bootsy", "groupe": "Parliament/Funkadelic", "cle": "Collins Bootsy"},
    {"nom": "Commerford", "prenom": "Tim", "groupe": "Rage Against The Machine", "cle": "Commerford Tim"},
    {"nom": "De Angelis", "prenom": "Victoria", "groupe": "Måneskin", "cle": "De Angelis Victoria"},
    {"nom": "Deacon", "prenom": "John", "groupe": "Queen", "cle": "Deacon John"},
    {"nom": "Deal", "prenom": "Kim", "groupe": "Pixies, The Breeders", "cle": "Deal Kim"},
    {"nom": "Dirnt", "prenom": "Mike", "groupe": "Green Day", "cle": "Dirnt Mike"},
    {"nom": "Dorsey", "prenom": "Gail Ann", "groupe": "David Bowie", "cle": "Dorsey Gail Ann"},
    {"nom": "Dupont", "prenom": "Fred", "groupe": "Studio, Rock français", "cle": "Dupont Fred"},
    {"nom": "East", "prenom": "Nathan", "groupe": "Eric Clapton, Daft Punk", "cle": "East Nathan"},
    {"nom": "Entwistle", "prenom": "John", "groupe": "The Who", "cle": "Entwistle John"},
    {"nom": "Feraud", "prenom": "Hadrien", "groupe": "John McLaughlin", "cle": "Feraud Hadrien"},
    {"nom": "Fiszman", "prenom": "Nicolas", "groupe": "Sting", "cle": "Fiszman Nicolas"},
    {"nom": "Fisher", "prenom": "Norwood", "groupe": "Fishbone", "cle": "Fisher Norwood"},
    {"nom": "Glover", "prenom": "Roger", "groupe": "Deep Purple", "cle": "Glover Roger"},
    {"nom": "Gordon", "prenom": "Mike", "groupe": "Phish", "cle": "Gordon Mike"},
    {"nom": "Graham", "prenom": "Larry", "groupe": "Sly & the Family Stone", "cle": "Graham Larry"},
    {"nom": "Harris", "prenom": "Steve", "groupe": "Iron Maiden", "cle": "Harris Steve"},
    {"nom": "Hellborg", "prenom": "Jonas", "groupe": "Solo, McLaughlin", "cle": "Hellborg Jonas"},
    {"nom": "Hoppus", "prenom": "Mark", "groupe": "Blink-182", "cle": "Hoppus Mark"},
    {"nom": "Hook", "prenom": "Peter", "groupe": "Joy Division, New Order", "cle": "Hook Peter"},
    {"nom": "Hurley", "prenom": "Sean", "groupe": "John Mayer, Studio", "cle": "Hurley Sean"},
    {"nom": "Jamerson", "prenom": "James", "groupe": "The Funk Brothers, Motown", "cle": "Jamerson James"},
    {"nom": "Jones", "prenom": "Darryl", "groupe": "Rolling Stones", "cle": "Jones Darryl"},
    {"nom": "Jones", "prenom": "John Paul", "groupe": "Led Zeppelin", "cle": "Jones John Paul"},
    {"nom": "Kajdan", "prenom": "Jean-Michel", "groupe": "Jazz fusion France", "cle": "Kajdan Jean-Michel"},
    {"nom": "Kanal", "prenom": "Tony", "groupe": "No Doubt", "cle": "Kanal Tony"},
    {"nom": "Kaye", "prenom": "Carol", "groupe": "The Wrecking Crew", "cle": "Kaye Carol"},
    {"nom": "Labaye", "prenom": "Romain", "groupe": "Scott Henderson", "cle": "Labaye Romain"},
    {"nom": "Lee", "prenom": "Will", "groupe": "Studio New York", "cle": "Lee Will"},
    {"nom": "Lesh", "prenom": "Phil", "groupe": "Grateful Dead", "cle": "Lesh Phil"},
    {"nom": "Levin", "prenom": "Tony", "groupe": "Peter Gabriel, King Crimson", "cle": "Levin Tony"},
    {"nom": "Lynott", "prenom": "Phil", "groupe": "Thin Lizzy", "cle": "Lynott Phil"},
    {"nom": "Maby", "prenom": "Graham", "groupe": "Joe Jackson", "cle": "Maby Graham"},
    {"nom": "Manring", "prenom": "Michael", "groupe": "Solo", "cle": "Manring Michael"},
    {"nom": "Mendel", "prenom": "Nate", "groupe": "Foo Fighters", "cle": "Mendel Nate"},
    {"nom": "McCartney", "prenom": "Paul", "groupe": "The Beatles", "cle": "McCartney Paul"},
    {"nom": "McKagan", "prenom": "Duff", "groupe": "Guns N' Roses", "cle": "McKagan Duff"},
    {"nom": "McVie", "prenom": "John", "groupe": "Fleetwood Mac", "cle": "McVie John"},
    {"nom": "Mbappé", "prenom": "Etienne", "groupe": "Joe Zawinul, Studio", "cle": "Mbappé Etienne"},
    {"nom": "Mendez", "prenom": "Martin", "groupe": "Opeth", "cle": "Mendez Martin"},
    {"nom": "Mienniel", "prenom": "Jocelyn", "groupe": "Electro Jazz", "cle": "Mienniel Jocelyn"},
    {"nom": "Miller", "prenom": "Marcus", "groupe": "Solo, Miles Davis", "cle": "Miller Marcus"},
    {"nom": "Morel", "prenom": "Jean-Philippe", "groupe": "Jazz français", "cle": "Morel Jean-Philippe"},
    {"nom": "Moutin", "prenom": "Louis", "groupe": "Trio Moutin", "cle": "Moutin Louis"},
    {"nom": "Mulot", "prenom": "Pascal", "groupe": "Shred Fusion", "cle": "Mulot Pascal"},
    {"nom": "Myung", "prenom": "John", "groupe": "Dream Theater", "cle": "Myung John"},
    {"nom": "Ndegeocello", "prenom": "Meshell", "groupe": "Solo", "cle": "Ndegeocello Meshell"},
    {"nom": "Newsted", "prenom": "Jason", "groupe": "Metallica", "cle": "Newsted Jason"},
    {"nom": "Paganotti", "prenom": "Bernard", "groupe": "Magma", "cle": "Paganotti Bernard"},
    {"nom": "Palladino", "prenom": "Pino", "groupe": "The Who, John Mayer", "cle": "Palladino Pino"},
    {"nom": "Pastorius", "prenom": "Jaco", "groupe": "Weather Report", "cle": "Pastorius Jaco"},
    {"nom": "Prestia", "prenom": "Rocco", "groupe": "Tower of Power", "cle": "Prestia Rocco"},
    {"nom": "Ramone", "prenom": "Dee Dee", "groupe": "The Ramones", "cle": "Ramone Dee Dee"},
    {"nom": "Rossi", "prenom": "Stéphan", "groupe": "Studio français", "cle": "Rossi Stéphan"},
    {"nom": "Rostand", "prenom": "Alexis", "groupe": "Variété/Funk", "cle": "Rostand Alexis"},
    {"nom": "Rutherford", "prenom": "Mike", "groupe": "Genesis", "cle": "Rutherford Mike"},
    {"nom": "Sabal-Lecco", "prenom": "Armand", "groupe": "Paul Simon, Studio", "cle": "Sabal-Lecco Armand"},
    {"nom": "Sklar", "prenom": "Leland", "groupe": "James Taylor, Studio US", "cle": "Sklar Leland"},
    {"nom": "Spalding", "prenom": "Esperanza", "groupe": "Jazz contemporain", "cle": "Spalding Esperanza"},
    {"nom": "Squire", "prenom": "Chris", "groupe": "Yes", "cle": "Squire Chris"},
    {"nom": "Taylor", "prenom": "John", "groupe": "Duran Duran", "cle": "Taylor John"},
    {"nom": "Texier", "prenom": "Henri", "groupe": "Jazz français, contrebasse", "cle": "Texier Henri"},
    {"nom": "Vernerey", "prenom": "Laurent", "groupe": "Studio France, Johnny Hallyday", "cle": "Vernerey Laurent"},
    {"nom": "Waters", "prenom": "Roger", "groupe": "Pink Floyd", "cle": "Waters Roger"},
    {"nom": "Weymouth", "prenom": "Tina", "groupe": "Talking Heads", "cle": "Weymouth Tina"},
    {"nom": "Wilkenfeld", "prenom": "Tal", "groupe": "Jeff Beck", "cle": "Wilkenfeld Tal"},
    {"nom": "Wimbish", "prenom": "Doug", "groupe": "Living Colour", "cle": "Wimbish Doug"},
    {"nom": "Wooten", "prenom": "Victor", "groupe": "Béla Fleck and the Flecktones", "cle": "Wooten Victor"},
    {"nom": "Young", "prenom": "Jennifer", "groupe": "Travis Larson Band", "cle": "Young Jennifer"},
    {"nom": "Zender", "prenom": "Stuart", "groupe": "Jamiroquai", "cle": "Zender Stuart"}
]
