liste = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7]

elementMax = liste[0]
nbMax = 0

for i in range(len(liste)):
    element = liste[i]

    compteur = 0
    for j in range(len(liste)):
        if liste[j] == element:
            compteur = compteur + 1

    if compteur > nbMax:
        nbMax = compteur
        elementMax = element

print("Le nombre le plus fréquent dans la liste est le :", elementMax, "(" + str(nbMax) + " x)")