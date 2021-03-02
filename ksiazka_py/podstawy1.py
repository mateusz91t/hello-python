from operator import itemgetter

# continue, break
print('\ncontinue, beak')
x, y = 3, 5
while True:
    x -= 1
    if x == 0:
        continue
    if x < -2:
        break
    print(y / x)

# string
print('\nstring')
s1 = '      nazwa firMYMY sp. z o.o.    '
print(s1)
print(s1.upper())
print(s1.capitalize())
print(s1.swapcase())
print(s1.casefold())
print(s1.islower())
print(s1.isupper())
print(s1.istitle())
print(s1.title())
print(s1.replace('o', '!'))
print(len(s1))
print('MY' in s1)
print(s1.count('MY'))
print(s1.strip())
print(s1.split())
print('_^_'.join(s1.split()))
print(s1 * 2)

if 'Python' > 'Java':
    print('to chyba jasne :) Tu jest miejsce na hejt: .........')
else:
    print('cos sie spsulo')

# slices
print('\nslices')
s2 = '0123456789'
print(s2)
print(s2[-1])
print(s2[2:5])
print(s2[2:9:3])
print(s2[:-3])
print(s2[:3])
print(s2[::3])
print(s2[::-1])

# lists
print('\nlists')
l1 = [7, 8, 'teksttekst']
l2 = ['234', 'a', 456, True, l1]
print(l2)
print('teksttekst' in l2)
print('teksttekst' in l1)
if 1 in l2:
    print('why?')

print(l1.append('X'))  # None
print(l1)
l2.insert(1, 'B')
print(l2)
print(l2.remove('a'))
print(l2)
l1.clear()
print(l2)

l3 = ['ogórek', 'pomidor', 'marchew', 'ziemniak']
print(l3)
l3.sort()
print(l3)
l3.reverse()
print(l3)

l3 = ['ogórek', 'pomidor', 'marchew', 'ziemniak']
l3.sort(reverse=True)
print(l3)

l4 = [[1, 'reno'], [4, 'cintronex'], [2, 'audi'], [3, 'zaporożec']]
print(l4)
l4.sort()
print(l4)
l4.sort(key=itemgetter(1))
print(l4)

l5 = [*range(2, 20, 3)]
print(l5)
print(sum(l5), max(l5), min(l5))
print(l5.index(17))

# map & filter
print('\nmap & filter')
l6 = list(map(lambda _: _ / 10, l5))
print(l6)
l7 = filter(lambda _: 1.5 > _ > 1, l6)
print(list(l7))

# tuple
print('\ntuple')
krotka = ('Tytanowy Janusz', 'Molibdenowy Mateusz', 'Przypadkowy Jarek', [12, 55, 'koza'])
print(krotka)
krotka2 = tuple()
print(krotka[2:4])

# dicts / maps
d1 = {'l1': l1, 'l2': l2, 'l3': l3}
print(d1)
print(d1['l2'])
for k in d1:
    print(k, d1[k])
print(d1.keys())
print(d1.values())
print(d1.items())
print(len(d1))
print('l1' in d1)
print(1 in d1)
d1[1] = 1.000001
print(1 in d1)
del d1[1]
print(1 in d1)

# sets
print('\nsets')
z1 = {1, 2, 1, 2, 1, 3}
print(z1)
z2 = {(1, 'B'), (2, 'D'), (3, 'A'), (4, 'C'), (4, 'C')}
print(z2)
z1.add(10)
print(10 in z1)
z1.remove(10)

z3 = {1, 2, 3, 4}
z4 = {3, 4, 5, 6, }

print(z3.union(z4))
print(z3)
z3.update(z4)
print(z3)

print("różnice")
z3 = {1, 2, 3, 4}
print(z3.difference(z4))
print(z3.symmetric_difference(z4))
print(z4.difference(z3))  # różnica
z3.difference_update(z4)
print(z3)

print("część wspólna")
z3 = {1, 2, 3, 4}
print(z3.intersection(z4))  # część wspólna
print(z3.isdisjoint(z4))
print({-1, -2, -3}.isdisjoint(z4))  # czy nie ma części wspólnej

print('subsets:')
z5 = {1, 2}
print(z3.issubset(z4))
print(z3.issuperset(z4))
print(z5.issubset(z3))
print(z3.issuperset(z5))
