def ele():
    yield 'ele 1'
    yield 'ele 2'
    yield 'ele 3'
    yield 'ele 4'


for e in ele():
    print(e)
print(*ele())


def mojzakres(numb):
    for x in range(numb):
        yield x * 10


print(*mojzakres(5))


def pows2(how_many: int):
    for _ in range(1, how_many + 1):
        yield 2 ** _


p1 = pows2(1000)
print(*p1)


def pows2ret(how_many: int):
    l1 = list()
    for _ in range(1, how_many + 1):
        l1.append(2 ** _)
    return l1


p2 = pows2ret(1000)
print(p2)

print(p1.__sizeof__())
print(p2.__sizeof__())
