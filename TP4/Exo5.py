date = input("Entrez une date au format jjmmaaaa : ")

while len(date) != 8 or not date.isdigit():
    print("Format incorrect : la date doit contenir exactement 8 chiffres (jjmmaaaa).")
    date = input("Entrez une date au format jjmmaaaa : ")

jour = int(date[0:2])
mois = int(date[2:4])
annee = int(date[4:8])

if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0:
    bissextile = True
else:
    bissextile = False

if annee < 1:
    print("Date invalide : l'année doit être supérieure ou égale à 0001.")
elif mois < 1 or mois > 12:
    print("Date invalide : le mois doit être compris entre 01 et 12.")
else:
    if mois == 2:
        if bissextile:
            joursMois = 29
        else:
            joursMois = 28
    elif mois == 4 or mois == 6 or mois == 9 or mois == 11:
        joursMois = 30
    else:
        joursMois = 31

    if jour < 1:
        print("Date invalide : le jour doit être supérieur ou égal à 01.")
    elif jour > joursMois:
        if mois == 2 and not bissextile:
            print("Date invalide : en", annee, "(année commune), février n'a que 28 jours.")
        elif mois == 2:
            print("Date invalide : en", annee, "(année bissextile), février n'a que 29 jours.")
        else:
            print("Date invalide : ce mois n'a que", joursMois, "jours.")
    else:
        print("La date", date[0:2] + "/" + date[2:4] + "/" + date[4:8], "est valide.")