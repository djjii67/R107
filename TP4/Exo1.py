import sys

if len(sys.argv) > 1:
    nombre = float(sys.argv[1])
else:
    nombre = float(input("Vous cherchez la table de multiplication de quel nombre ? "))

resultats = []
for i in range(10):
    resultats.append(round(nombre * i, 1))

for i in range(len(resultats)):
    print(nombre, "*", i, "=", resultats[i])