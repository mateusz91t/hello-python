from locale import getpreferredencoding
from os.path import getsize
from typing import TextIO

print(getpreferredencoding())  # cp1250
sciezka = 'files_sources/dane.txt'
print(getsize(sciezka))  # 59 bajtów
print(sciezka.__sizeof__())  # 59 bajtów


plik = open(sciezka)
print(plik.readlines()[5])
plik.close()

plik2 = open(sciezka, encoding='utf8')
print(plik2.readlines()[5])
plik2.close()

print('\npo ilości bajtów:')
plik3 = open(sciezka, encoding='utf8')
linie3 = plik3.read(20)
print(linie3)
print('*' * 20)
linie3 = plik3.read(20)
print(linie3)
plik3.close()

print('\nreadlines() vs read().splitlines():')
plik4 = open(sciezka, encoding='utf8')
print(plik4.readlines())
plik4.seek(0)  # default to 0, czyli początek
print(plik4.read().splitlines())
plik4.close()

# mode = 'a' i 'w' tworzą plik jeśli go nie ma
# 'r+' czyta i nadpisuje, ale nie tworzy
sciezka2: str = 'files_sources/nowy.txt'
plik5: TextIO = open(sciezka2, mode='r+')
plik5.write('haHAHAho\n')
plik5.close()
print()
