inf10 = 0
sup10 = 0
entre = 0
for i in range(10):
    n = float(input("Rentrez une valeur :"))
    while n < 0 or n > 20:
        n = float(input("Valeur incorrect :"))
    if n < 10:
        inf10 = inf10 + 1
    elif n < 15:
        entre = entre + 1
    else :
        sup10 = sup10 + 1
print("Votre valeur est inférieur à 10 :", inf10)
print("Votre valeur est supérieur à 10 :", sup10)
print("Votre valeur est entre 10 et 15:", entre)