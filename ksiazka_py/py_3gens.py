def ele():
    yield 'ele 1'
    yield 'ele 2'
    yield 'ele 3'
    yield 'ele 4'


print(*ele())
for e in ele():
    print(e)


def mojzakres(numb):
    for x in range(numb):
        yield x * 10


print(*mojzakres(5))


def pows2(how_many: int):
    for _ in range(1, how_many + 1):
        yield 2 ** _


p1 = pows2(10)
print(*p1)


def pows2ret(how_many: int):
    l1 = list()
    for _ in range(1, how_many + 1):
        l1.append(2 ** _)
    return l1


p2 = pows2ret(10)
print(p2)

print(p1.__sizeof__())
print(p2.__sizeof__())


def dyszki():
    x = 1
    while True:
        yield x * 10
        x += 1


d1 = dyszki()
print(next(dyszki()), id(dyszki()))
print(next(dyszki()), id(dyszki()))
print(next(d1), id(d1))
print(next(d1), id(d1))
print(d1.__next__())
print(d1.__next__())


def wczytajduzyplik(sciezka: str, separator: str = ''):
    with open(file=sciezka, mode='r') as plik:
        while True:
            linia = plik.readline()
            if linia:
                if separator:
                    yield linia.strip().split(separator)
                else:
                    yield linia
            else:
                break


f1 = wczytajduzyplik('files_sources/dane.csv', ';')
print(next(f1))
print(type(f1))
