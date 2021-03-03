import xml.etree.ElementTree as Et


drzewo = Et.parse('../../files_sources/dane.xml')
print(type(drzewo))
root = drzewo.getroot()
print(type(root), root)
imie = root.find('imie')
print(type(imie), imie, imie.text)
adres = root.find('adres')
miasto = adres.find('miasto')
print(miasto.text)
nazwisko = root.find('nazwisko')
print(nazwisko.text)
print(nazwisko.attrib)

print(root[0].tag, root[1].tag)
print(root[0].text, root[1].text)
print(root[3][1].text)

for x in root.findall('jezyki'):
    print(x, type(x), x.text)

print(Et.tostring(imie))
print(Et.tostring(root))
