class Sing:
    pass


print('\nsing')
s1 = Sing()
s2 = Sing()
print(s1, id(s1))
print(s2, id(s2))
print(s1 is s2)


class Sing2:
    __instancja = None
    pole = None

    def __new__(cls, *args, **kwargs):
        if cls.__instancja is None:
            cls.__instancja = super().__new__(cls, *args, **kwargs)
        return cls.__instancja


print('\nsing2')
s3 = Sing2()
s4 = Sing2()
print(s3, id(s3))
print(s4, id(s4))
print(s3 is s4)
s3.pole = 5
print(s4.pole)


class BazodanowyPolaczyciel:
    polaczenie = None
    instancja = None

    def __new__(cls, *args, **kwargs):
        if cls.instancja is None:
            print('Nawiązywanie połączenia')
            cls.polaczenie = 'połączenie do takiej a takiej bazy'
            cls.instancja = super().__new__(cls, *args, **kwargs)
        print('Połączono...')
        return cls.instancja


bp1 = BazodanowyPolaczyciel()
BazodanowyPolaczyciel()
bp2 = BazodanowyPolaczyciel()

print(bp2 is bp1)
print(bp1.instancja, bp1.polaczenie)
print(bp2.instancja, bp2.polaczenie)
