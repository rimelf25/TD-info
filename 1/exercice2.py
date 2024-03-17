from exercice1 import exercice1
def lireMotsPossibles():
    """Cette fonction renvoie une liste des mots du lexique français à partir du fichier frenchssaccent.dic"""
    mots = []
    f = open("frenchssaccent.dic", 'r')
    for ligne in f:
        mots.append(ligne[0:len(ligne)-1])
    f.close()
    return mots

def exercice2(tirage):
    """cette fonction prend en arg une liste de lettres et répond à l'exercice 2"""
    motsPossibles = lireMotsPossibles()
    #comme au 1er exo
    return exercice1(tirage, motsPossibles)

#Tests => voir le fichier tests.py

