import exercice1, exercice2, exercice3, exercice4

#Tests:
#Données

tirage1 = ['b', 'p', 'd', 'w', 's', 'y', 'w', 'i']
motsPossibles1 = ['bis', 'bd']
tirage2 = ['a', 'r', 'b', 'g', 'e', 's', 'c', 'j']
motsPossibles2 = ['sacre', 'sabre', 'baser', 'cabre', 'garce', 'crase', 'brase', 'barge', 'caser', 'jaser', 'crabe', 'scare', 'aber', 'gare', 'sage', 'gars', 'rase', 'arec', 'acre', 'jars', 'case', 'base', 'cage', 'rage', 'jase', 'bras', 'race', 'ars', 'sac', 'arc', 'are', 'jar', 'jas', 'bar', 'bas', 'ace', 'cas', 'car', 'age', 'bac', 'cab', 'as', 'ra', 'sa', 'a']
tirage3 = list('zxcvrrt?')

print("Tests: exercice 1 =======\n")

print("Test1:\n"
      f"Tirage1: {tirage1}\n"
      f"Mots Possibles: {motsPossibles1}")
print("Resultat1: " + exercice1.exercice1(tirage1, motsPossibles1))

print("\nTest2:\n"
      f"Tirage2: {tirage2}\n"
      f"Mots Possibles2: {motsPossibles2}")

print("Resultat2: " + exercice1.exercice1(tirage2, motsPossibles2))


print("\n\nTests: exercice 2 ========\n")

print("Test1:\n"
      f"Tirage1: {tirage1}")
print("Resultat1: " + exercice2.exercice2(tirage1))

print("\nTest2:\n"
      f"Tirage2: {tirage2}")
print("Resultat2: " + exercice2.exercice2(tirage2))

print("\n\nTests: exercice 3 ========\n")


print("Tests scoreMot(mot):\n")
print("score('lettre'): " + str(exercice3.scoreMot('lettre')))
print("score('scrabble'): " + str(exercice3.scoreMot('scrabble')))

print("\nTest1:\n"
      f"Tirage1: {tirage1}")
print("Resultat2: " + str(exercice3.exercice3(tirage1)))

print("\nTest2:\n"
      f"Tirage2: {tirage2}")
print("Resultat2: " + str(exercice3.exercice3(tirage2)))

print("\n\nTests: exercice 4 ========\n")

print("Test1:\n"
      f"Tirage1: {tirage1}")
print("Resultat1: " + str(exercice4.exercice4(tirage1)))

print("\nTest2:\n"
      f"Tirage2: {tirage2}")
print("Resultat2: " + str(exercice4.exercice4(tirage2)))

print("\nTest2:\n"
      f"Tirage2: {tirage3}")
print("Resultat2: " + str(exercice4.exercice4(tirage3)))