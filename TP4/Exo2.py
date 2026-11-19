nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
notes = []

for i in range(nombreEtudiants):
    note = float(input("Note etudiant " + str(i) + " : "))

    while note < 0 or note > 20:
        print("Erreur : la note doit etre comprise entre 0 et 20 !")
        note = float(input("Note étudiant " + str(i) + " : "))

    notes.append(note)
    moyenne = moyenne + note

moyenne = moyenne / nombreEtudiants
print()
print("Moyenne de classe :", moyenne)
print()

print("Numéro de l'etudiant | note | ecart à la moyenne")
for i in range(nombreEtudiants):
    ecart = notes[i] - moyenne
    print(i, "|", notes[i], "|", ecart)