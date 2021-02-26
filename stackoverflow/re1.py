class Cl1:
    def __init__(self, name='Jan', age=20):
        self.name = name
        self.age = age

    def hello(self, tekst='siema'):
        print(tekst)
        print(self._get_data())

    def _get_data(self):
        print('_get_data from C1')
        return f'{self.name} {self.age}'


class Cl2(Cl1):
    def __init__(self, name='Jan', age=20):
        super().__init__(name, age)

    def _get_data(self):
        print('_get_data from C2')
        return f'{self.name} {self.age}'


cl1_1 = Cl1('Ignacy')
cl2_1 = Cl2(age=15)

cl1_1.hello()
print(20 * '-')
cl2_1.hello('yoyo')