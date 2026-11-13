import random

x = random.randint(0, 100)

tentatives = 0
proposition = -1


while proposition != x:
    proposition = int(input("Entrez votre proposition (entre 0 et 100) : "))

    tentatives = tentatives + 1

    if proposition < x:
        print("C'est plus grand !\n")
    elif proposition > x:
        print("C'est plus petit !\n")
    else:
        print(f"Bravo ! Vous avez trouvé le nombre mystère {x} !")
        print(f"Nombre de tours nécessaires : {tentatives}")