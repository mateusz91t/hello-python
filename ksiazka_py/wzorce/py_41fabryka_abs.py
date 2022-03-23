from abc import ABC, abstractmethod


class Samochod(ABC):
    @abstractmethod
    def jedz(self):
        pass


class SamochodSportowy(Samochod):
    def jedz(self):
        print('sportowy wydech robi WRUUM')


class Limuzyna(Samochod):
    def jedz(self):
        print('cicho jedzie')


class SamochodMiejski(Samochod):
    def jedz(self):
        print('pyr pyr pyr...')


class FabrykaSamochodow(ABC):
    @abstractmethod
    def produkuj_samochod(self):
        pass


class FabrykaAutSportowych(FabrykaSamochodow):
    def produkuj_samochod(self):
        return SamochodSportowy()


class FabrykaLimuzyn(FabrykaSamochodow):
    def produkuj_samochod(self):
        return Limuzyna()


class FabrykaAutMiejskich(FabrykaSamochodow):
    def produkuj_samochod(self):
        return SamochodMiejski()
