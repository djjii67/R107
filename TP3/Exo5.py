n = int(input("Entrez un nombre entier n positif : "))

print("Choisissez la structure itérative à utiliser :")
print("1. Boucle 'for'")
print("2. Boucle 'while'")
choix = input("Votre choix (1 ou 2) : ")

fact = 1

if choix == '1':
    print(f"\n--- Calcul de {n}! avec la boucle FOR ---")
    for i in range(1, n + 1):
        fact = fact * i
        print(f"Étape i = {i} -> factorielle = {fact}")

    print(f"\nRésultat final : {n}! = {fact}")

elif choix == '2':
    print(f"\n--- Calcul de {n}! avec la boucle WHILE ---")
    i = 1
    while i <= n:
        fact = fact * i
        print(f"Étape i = {i} -> factorielle = {fact}")
        i = i + 1
    print(f"\nRésultat final : {n}! = {fact}")

else:
    print("Choix invalide ! Veuillez relancer le programme et choisir 1 ou 2.")