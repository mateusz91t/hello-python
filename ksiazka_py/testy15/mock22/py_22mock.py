from unittest import mock


makieta = mock.Mock()
makieta.pole1 = 20
makieta.pole2 = 'Element testowy'
print('pole1 = {}, pole2 = {}'.format(makieta.pole1, makieta.pole2))

makieta.dawaj_pi.return_value = 3.14
print(makieta.dawaj_pi)
print(makieta.dawaj_pi())