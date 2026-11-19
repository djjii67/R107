nMax = 10

v1 = []
v2 = []

n = int(input("Quelle est la taille de vos vecteurs [entre 1 et " + str(nMax) + "] ? "))

while n < 1 or n > nMax:
    n = int(input("Quelle est la taille de vos vecteurs [entre 1 et " + str(nMax) + "] ? "))

print()
print("Saisie du premier vecteur :")
for i in range(n):
    composante = int(input("v1[" + str(i) + "] = "))
    v1.append(composante)

print()
print("Saisie du second vecteur :")
for i in range(n):
    composante = int(input("v2[" + str(i) + "] = "))
    v2.append(composante)

produit = 0
for i in range(n):
    produit = produit + v1[i] * v2[i]

print()
print("Le produit scalaire de v1 par v2 vaut", produit)