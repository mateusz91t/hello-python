from collections import Counter
from operator import itemgetter
import random
import string
import re


l1 = list(x for x in range(20) if x % 2 == 0)
list(filter(lambda x: x % 4 == 0, l1))
l2 = list(map(lambda x: x+1, l1))
l1, l2
len(list(zip(l1, l2))), list(zip(l1, l2))

l3 = l1.copy()
l3.extend(l2)
l3.sort()

l3[::-1]
l3[-3:]
l3[-3]

l4 = list(string.ascii_lowercase)
l4

l5 = [l4[random.randint(0, len(l4) - 1)] for x in range(50)]

l5
l6 = dict(Counter(l5))
l6

l7 = ['a'] * 3
l7

a, b, c = 'cZeŚć zaaaa awW wa', 2, 3
print("tekst {}".format(a))
print(f"tekst {a}")
print(f"tekst {a.capitalize()}")
print(f"tekst {a.title()}")
print(f"tekst {a.replace('a','-')}")
f'{a}'
len(a)
'_'.join(a)

True if 'Z' in a else False
print(l4[:])
print(l4)

l4.insert(1, ['1', '2'])
l4
del l4[1:3]
l4.insert(1, 'b')
l4.__len__()
l8 = list(zip(l4, range(26, 0, -1)))
l8.sort(key=itemgetter(1))  # sortowanie po drugim elemencie
l8

a, b = b, a
a, b
l9 = list(map(lambda x: list(x)[::-1], l8))
l9
d1 = dict(l9)
d1
d1[1]
d1.get(0)
d1.get(1)
d1.get('1', 'łabaaa')  # return what you want if element not in d1
d1.items()
list(d1.items())[6]
d1.values()
d1.keys()

# ex
# 1/0

try:
    # 1/0
    # l1[20]
    # raise TypeError
    print(2 + 1)
except (ZeroDivisionError, IndexError) as z:
    print('catched ZeroDivisionError or IndexError')
    print(f'message: {z}')
except:
    print('catched other')
else:
    print('no errors')

# funkcja jako argument
b


def upp(txt: str) -> str:
    return txt.upper()


def apply_to_all(func, *args):
    for el in args:
        print(func(el))


apply_to_all(upp, b)


def wybierz(powieksz_pomniejsz_przemnoz):
    def pomniejsz(txt: str) -> str:
        return txt.lower()

    def powieksz(txt: str) -> str:
        return txt.upper()

    def przemnoz(txt: str, razy: int) -> str:
        return txt * razy

    defs = {'pomniejsz': pomniejsz, 'powieksz': powieksz,
            'przemnoz': przemnoz}
    return defs.get(powieksz_pomniejsz_przemnoz)


pow = wybierz('powieksz')
pow(b)
wybierz('przemnoz')(b, 3)

# re
b
wzorzec = ' ?[a-z]*[A-Z]*[a-z]* ?'
re.findall(wzorzec, b)

