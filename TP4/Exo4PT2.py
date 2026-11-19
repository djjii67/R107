liste = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7]

elementMax = liste[0]
nbMax = liste.count(elementMax)

for element in liste:
    compteur = liste.count(element)
    if compteur > nbMax:
        nbMax = compteur
        elementMax = element

print("Le nombre le plus fréquent dans la liste est le :", elementMax, "(" + str(nbMax) + " x)")