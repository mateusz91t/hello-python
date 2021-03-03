import json


sciezka1 = '../../files_sources/dane.json'
plik1 = open(sciezka1, encoding='utf8')
json1 = json.load(plik1)

print(type(json1))
print(json1)
print(json1['imie'])
print(json1['adres'])
print(json1['adres']['kod'])

for k in json1.keys():
    print(k, json1[k])
for v in json1['jezyki']:
    print(v)

print()
print(json1['jezyki'][2])

