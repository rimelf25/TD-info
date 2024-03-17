from exercice3 import scoreLettres, exercice3

def exercice4(tirage:list):
    """Cette fonction prend en argument une liste de lettres (tirage) et gère le cas du joker"""
    if "?" not in tirage:  # Le cas déjà traité à la question 3
        return exercice3(tirage)
    else:  # Le cas où on a le joker ?
        tirage.remove("?")
        resultatsTirageJoker = []

        # Je remplace le ? par chaque lettre et je garde le meilleur résultat, je l'ajoute à la liste des résultats de chque tirage. Enfin je renvoie le meilleur parmi tous les résultats
        for lettre in scoreLettres.keys():
            nouveauTirage = tirage + [lettre]
            resultat = exercice3(nouveauTirage)
            # le joker = 0
            resultat = (resultat[0], resultat[1] - scoreLettres[lettre])
            resultatsTirageJoker.append(resultat)

        resultatsTirageJoker.sort(key=lambda res: res[1], reverse=True)
        return resultatsTirageJoker[0]

#Tests => voir le fichier tests.py