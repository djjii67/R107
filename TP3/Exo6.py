debut = int(input("Heure de debut : "))
fin = int(input("Heure de fin : "))

if debut < 0 or debut > 24 or fin < 0 or fin > 24:
    print("Les heures doivent etre comprises entre 0 et 24 !")

elif debut == fin:
    print("Attention ! l’heure de fin est identique à l’heure de debut.")

elif debut > fin:
    print("Attention ! le debut de la location est apres la fin ...")

else:
    total_prix = 0

    for heure in range(debut, fin):
        if (0 <= heure < 7) or (17 <= heure < 24):
            total_prix += 1
        else:
            total_prix += 2


    print(f"Le montant de la location est de {total_prix} euros.")