from abc import ABC, abstractmethod


class Figura(ABC):
    nazwa = None

    def pokaz_nazwe(self):
        print(self.nazwa)

    @abstractmethod
    def oblicz_pole(self):
        pass


class Kwadrat(Figura):
    def __init__(self, dlugosc_boku):
        self.__dlugosc_boku = dlugosc_boku
        self.nazwa = Kwadrat.__name__

    def oblicz_pole(self):
        return self.__dlugosc_boku ** 2


class Prostokat(Figura):
    def __init__(self, bok_a, bok_b):
        self.bok_a = bok_a
        self.bok_b = bok_b
        self.nazwa = Prostokat.__name__

    def oblicz_pole(self):
        return self.bok_a * self.bok_b


# f1 = Figura()  # @abstractmethod uniemożliwia utowrzenie obiektu
k1 = Kwadrat(4)
p1 = Prostokat(3, 8)
print(k1.nazwa, k1.oblicz_pole())
print(p1.nazwa, p1.oblicz_pole())
