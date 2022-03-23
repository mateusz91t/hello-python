import re

t1 = 'Łęcki-Kąt'

p1 = re.compile(r'([A-Za-zĄąĆćĘęŁłŃńÓóŚśŹźŻż])')

m1 = p1.match(t1)
f1 = p1.findall(t1)

print(m1)
print(len(f1))
print(f1)
