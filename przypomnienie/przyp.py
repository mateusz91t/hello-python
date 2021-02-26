i1 = 5
i2 = 6
i3 = i1 + i2
print(id(i1), id(i2), id(i3))
i1 +=1
print(id(i1), id(i2), id(i3))

b1 = True
b2 = False
print(id(b1), id(b2))
b1 = False
b2 = True
print(id(b2), id(b1))

t1 = 'tekst1'
t2 = "tekst2"

if i1 > i2:
    print(i1, 'jest większe')
elif i1 < i2:
    print(i2, 'jest większe')
else:
    print(i1, 'i', i2, 'są równe')

# co to robi?
cp1 = compile('przyp.py','przy1.py', 'exec')
print(cp1)

# liczby zespolone
com1 = complex(0.1, 0.1)

print(com1 + com1 + com1)

t1 = 'tekst1'
l1 = [_ for _ in t1]
print(
    'l1 =\n',
    l1
)

seasons = ['winter', 'spring', 'summer', 'autumn']

ms1 = map(lambda x: x[0] > 'j', seasons)

l2 = list(range(1, 10))
l3 = list(range(10, 100, 10))
print(l2)
print(l3)
l4 = list(map(lambda x, y: x + y, l2, l3))
print(l4)

