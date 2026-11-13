debut = int(input("Entrez l'heure de debut (entre 0 et 24) : "))
fin = int(input("Entrez l'heure de fin (entre 0 et 24) : "))

if debut < 0 or debut > 24 or fin < 0 or fin > 24 or debut >= fin:
    print("Erreur : Les heures saisies sont incorrectes ou la fin précède le début.")
else:
    total_prix = 0

    for heure in range(debut, fin):
        if (heure >= 0 and heure < 7) or (heure >= 17 and heure < 24):
            total_prix = total_prix + 1
        else:
            total_prix = total_prix + 2

    print(f"\nDuree de la location : de {debut}h a {fin}h")
    print(f"Le montant total a payer est de : {total_prix} euros.")