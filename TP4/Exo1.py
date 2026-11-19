nombre = float(input("Vous cherchez la table de multiplication de quel nombre ? "))

resultats = []

for i in range(10):
    resultat = round(nombre * i, 1)
    resultats.append(resultat)

for i in range(10):
    print(nombre, "*", i, "=", resultats[i])