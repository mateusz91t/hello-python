import py_41fabryka_abs as fa

# s1 = fa.Samochod()  # nie da się zainicjalizować obiektu klasy ABC abstrakcyjnej
s2 = fa.SamochodSportowy()
s3 = fa.Limuzyna()
s4 = fa.SamochodMiejski()

ls = [fa.SamochodMiejski(), s2, s3, s4]
for auto in ls:
    auto.jedz()

print('\nfabryka')
# rodzaj = 'miejski'
# rodzaj = 'sportowy'
rodzaj = 'limuzyna'
if rodzaj == 'sportowy':
    fabryka = fa.FabrykaAutSportowych()
elif rodzaj == 'limuzyna':
    fabryka = fa.FabrykaLimuzyn()
elif rodzaj == 'miejski':
    fabryka = fa.FabrykaAutMiejskich()
else:
    NotImplementedError(f'nie ma fabryki dla auta {rodzaj}')

s5 = fabryka.produkuj_samochod()
s5.jedz()
