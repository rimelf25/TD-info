from exercice2 import lireMotsPossibles

# score de chaque lettre
scoreLettres = {"a": 1,
                "e": 1,
                "i": 1,
                "l": 1,
                "n": 1,
                "o": 1,
                "r": 1,
                "s": 1,
                "t": 1,
                "u": 1,
                "d": 2,
                "g": 2,
                "m": 2,
                "b": 3,
                "c": 3,
                "p": 3,
                "f": 4,
                "h": 4,
                "v": 4,
                "j": 8,
                "q": 8,
                "k": 10,
                "w": 10,
                "x": 10,
                "y": 10,
                "z": 10,
                "?":0}

def scoreMot(mot):
    """Cette fonction calcule le score du mot passé en argument"""
    score = 0
    for lettre in mot:
        score += scoreLettres[lettre]
    return score

def exercice3(tirage):
    """cette fonction prend en arg une liste de lettres et répond à l'exercice 3"""
    motsPossibles = lireMotsPossibles()
    mots = []
    for mot in motsPossibles:
        ajouter = True
        for lettre in mot:
            if lettre not in tirage or mot.count(lettre) > tirage.count(lettre):
                ajouter = False
        if ajouter:
            mots.append(mot)
    mots.sort(key=lambda mot:scoreMot(mot), reverse= True)
    return mots[0], scoreMot(mots[0])

#Tests => voir le fichier tests.py