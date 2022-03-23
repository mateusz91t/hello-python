def wyszukiwanie_binarne(lista: list, x: int):
    od = 0
    do = len(lista)

    while od <= do:
        srodek = 1 + int(do/2)
        if x == lista[srodek]:
            return srodek
        elif lista[srodek] > x:
            do = srodek - 1
        else:
            od = srodek + 1
    return -1


l1 = [1, 3, 4, 6, 10, 11, 12, 13]

print(wyszukiwanie_binarne(l1, 6))
