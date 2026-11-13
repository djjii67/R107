
x = int(input("Entrez un nombre X supérieur à 1 : "))

somme = 0
n = 0

while somme + (n + 1) <= x:
    n = n + 1
    somme = somme + n

print("Le plus grand nombre N est :", n)
print(f"Vérification : la somme vaut {somme}")