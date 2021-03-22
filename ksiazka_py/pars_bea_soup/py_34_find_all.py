from py_32bea_soup import zupa


for tag in zupa.findAll():
    print(tag.name)

print('\ntype', type(zupa.findAll()))

for tag in zupa.findAll('a'):
    print(tag)

print('\nlen', len(zupa.findAll('a')))

for tag in zupa.findAll(attrs={'class': 'imInvisible'}):
    print(tag.name, tag.string)

print('\ncontents')
lista = zupa.find(id='imBody').contents
print(lista)
print(len(lista))
print(type(lista))
print(lista[3])

print('\ncontets of contents')
print(lista[1].contents[5].contents[1].contents[1].a.string)
