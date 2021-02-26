from przypomnienie.MyError123 import MyError1


class Cl:
    def __init__(self, name, age, lista=None):
        if lista is None:
            self.lista = list()
        else:
            self.lista = lista
        self.age = age
        self.name = name

    def __add__(self, other):
        if isinstance(other, Cl):
            c = Cl('1: %r 2: %r' % (self.name, other.name), self.age + other.age)
        else:
            c = Cl(self.name, self.age + other)
        return c

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        self.age += other
        return self

    def __str__(self):
        return 'imię: %r\twiek: %r\tlista: %r'\
               % (self.name, self.age, self.lista)

    def __getitem__(self, item):
        return self.lista[item]

    def __setitem__(self, key, value):
        # self.lista[key] = value
        raise MyError1(key, value)

    def __len__(self):
        return len(self.lista)

    def __missing__(self, key):
        return 'There is no %r element' % key


c1 = Cl('Jan', 2)
c2 = Cl('Iwan', 4)

print(c1 + c2)
print(c1 + 1)
print(2 + c1)
print(
    'c1, id(c1)=\n',
    c1, id(c1)
)
c1 += 1
print(
    'c1, id(c1)=\n',
    c1, id(c1)
)

c3 = Cl('San', 1, [1, 2, 3])
print(c3)

print(c3[2])
c3[2] = 'a'
print(c3)
print(len(c3))
# print(c3[10])

