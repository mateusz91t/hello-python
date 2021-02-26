class A:
    pass


class B(A):
    pass


class C(B):
    pass


a: A = A()
b: B = B()

print(isinstance(a, A))
print(isinstance(B, A))
print(isinstance(A, B))

print()
print(issubclass(B, A))
print(issubclass(A, B))

c: C = C()
print()
print(isinstance(c, A))
print(isinstance(c, B))
print(isinstance(c, C))

print()
print(issubclass(C, A))


class Baza:
    def who_am_i(self):
        self.primitive_who_am_i()
        self.detailed_who_am_i()

    def primitive_who_am_i(self):
        print("nazwa Baza")

    def detailed_who_am_i(self):
        print('self.__class__.__name__: ', self.__class__.__name__)


class Potomek(Baza):  # Potomek dziedziczy po Baza
    def primitive_who_am_i(self):
        tata = super()
        print('type(tata) =', type(tata))
        tata.primitive_who_am_i()
        print("nazwa Potomek")


baza = Baza()
potomek = Potomek()

potomek.primitive_who_am_i()
