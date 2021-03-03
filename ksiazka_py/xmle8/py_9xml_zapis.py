import xml.etree.cElementTree as Et


# cElementTree is optimized, ElementTree is not
# text update
r = Et.parse('../../files_sources/dane.xml').getroot()
for e in r:
    print(e.tag, e.attrib, e.text)

r.find('nazwisko').text = 'Kowalski po zmianie'

print('-' * 20, 'text update:')
for e in r:
    print(e.tag, e.attrib, e.text)

# add / del / upd params
print('-' * 20, 'add / del / upd params:')
r.find('nazwisko').attrib['enc'] = 'utf8'
del r.find('nazwisko').attrib['param']
for e in r:
    print(e.tag, e.attrib, e.text)

# add elements #1
Et.SubElement(r, 'masa').text = '72.4'  # dodaje elems na końcu
Et.SubElement(r.find('adres'), 'ulica').text = 'Bura'
print('-' * 20, 'add elements #1:')
for e in r:
    print(e.tag, e.attrib, e.text)

# add els #2
auto = Et.Element('samochod')
auto.text = 'Renia Clio'
r.insert(2, auto)  # dodaje els na wybrane miejsce
print('-' * 20, 'add elements #2:')
for e in r:
    print(e.tag, e.attrib, e.text)

# del elements
del r[0]
r.remove(r.find('jezyki'))
print('-' * 20, 'del elements:')
for e in r:
    print(e.tag, e.attrib, e.text)


# save
print(Et.tostring(r))
et = Et.ElementTree(r)
et.write('../../files_sources/dane2.xml', encoding='utf8')
