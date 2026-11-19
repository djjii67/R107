tab = [5, 2, 4, 8, 1, 3]
n = len(tab)

print(tab)

for i in range(n - 1):
    indiceMin = i
    for j in range(i + 1, n):
        if tab[j] < tab[indiceMin]:
            indiceMin = j

    temp = tab[i]
    tab[i] = tab[indiceMin]
    tab[indiceMin] = temp

    print(tab)