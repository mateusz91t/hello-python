class Owoc:
    click = 5

    def __init__(self, kolor='brak'):
        self.kolor = kolor

    def zjedz(self, ile):
        print('zjedz cały {}'.format(ile))

    def zjedz(self):  # jeśli ta f będzie pierwsza zadeklarowana to się wysypie
        print('zjedz cały')

    @staticmethod
    def statyczna():
        print('statyczna metoda')


o1 = Owoc()
o2 = Owoc()

print(o1 == o2)

o1.zjedz()
# o1.zjedz(ile=2)  # to nie zadziała, bo metoda z 'ile' została przesłonięta, a nie przeciążona

o1.statyczna()
Owoc.statyczna()
# Owoc.zjedz()  # wysypie się bo jest self w def, którego klasa nie ma
