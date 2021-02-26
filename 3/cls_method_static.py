# class methods ~= static methods

class Cat:
    def __init__(self, name: str = 'Cotte', weight: int = 3):
        print('jestem w __init__')
        print('type(self) =', type(self))
        print('self =', self)
        self.name = name
        self.weight = weight

    def do_sth(self):
        print('jestem w do_sth')
        print('type(self) =', type(self))
        print('self =', self)

    @classmethod
    def stat_method(cls, your_text: str = 'something...'):
        print('jestem w stat_method', your_text)
        print('type(self) =', type(cls))
        print('self =', cls)


print('\ncat_1: Cat = Cat() =')
cat_1: Cat = Cat()

print('\nCat.do_sth(Cat) =')
Cat.do_sth(Cat)

print('\nCat.do_sth(cat_1) =')
Cat.do_sth(cat_1)

print('\ncat_1.stat_method() =')
print(cat_1.stat_method())

print('\nCat.stat_method() =')
print(Cat.stat_method())
