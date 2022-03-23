from py_32bea_soup import strona, zupa

print(strona)
print(zupa.h1)
print(type(zupa.h1))
print(zupa.find('h1'))
print(type(zupa.find('h1')))

print('\npo id')
print(zupa.find(id="imHeader"))

print('\npo klasie css')
# print(zupa.find(class = 'imInvisible'))  # nie działa - chce zakładać klasę??
print(zupa.find(attrs={'class': 'imInvisible'}))

print('\npo attrs działa')
print(zupa.find(attrs={'name':'imGoToCont'}))

print('\nzagnieżdżenia')
print( zupa.find(id="imBody").li.a )

print('\npo sekcjach strony')
print(zupa.title)

print('\nhead')
print(zupa.head)

print('\nbody')
print(zupa.body)

print('\na attrs')
print(zupa.body.li.a.attrs)
print(type(zupa.body.li.a.attrs))
print(zupa.body.li.a.attrs['href'])
print(type(zupa.body.li.a.attrs['href']))

print('\ntyp elementu i str elementu znalezionego po np. id')
print(zupa.find(id='imBody').name)
print(zupa.find(id='imBody').string)  # to tylko kontener więc nie ma tekstu
print(zupa.p)
print(zupa.p.string)
