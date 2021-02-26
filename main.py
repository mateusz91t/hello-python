from collections import Counter

d_1: dict = {'eur': 5, 'pln': 2.3}

print(d_1)
print(dict(Counter(d_1) + Counter(d_1)))

for x, y in d_1.items():
    print(x, y)

print(d_1.__contains__('eur'))

print(d_1)
d_1['eur'] += -3
print(d_1)
print(d_1)