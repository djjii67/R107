debut = int(input("Donnez l’heure de debut de la location (un entier) : "))
fin = int(input("Donnez l’heure de fin de la location (un entier) : "))

if debut < 0 or debut > 24 or fin < 0 or fin > 24:
    print("Les heures doivent être comprises entre 0 et 24 !")

elif debut == fin:
    print("Attention ! l’heure de fin est identique à l’heure de début.")

elif debut > fin:
    print("Attention ! le début de la location est après la fin ...")

else:
    nb_heures_tarif1 = 0
    nb_heures_tarif2 = 0

    for heure in range(debut, fin):
        if (0 <= heure < 7) or (17 <= heure < 24):
            nb_heures_tarif1 += 1
        else:
            nb_heures_tarif2 += 1

    total_prix = (nb_heures_tarif1 * 1.0) + (nb_heures_tarif2 * 2.0)

    print("Vous avez loue votre velo pendant")
    if nb_heures_tarif1 > 0:
        print(f"{nb_heures_tarif1} heure(s) au tarif horaire de 1.0 euro(s)")
    if nb_heures_tarif2 > 0:
        print(f"{nb_heures_tarif2} heure(s) au tarif horaire de 2.0 euro(s)")
    print(f"Le montant total a payer est de {total_prix} euro(s).")