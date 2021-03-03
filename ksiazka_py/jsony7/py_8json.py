import json


d1 = dict()
d1['ksiazka'] = 'Finansowy Ninją'
d1['film_na_wieczor'] = 'https://www.youtube.com/watch?v=sCNrK-n68CM'
d1['banknony'] = [10, 20, 50, 100, 200, 500]
print(d1)
for k in d1:
    print(k, d1[k])
f1 = open('../../files_sources/jsonout.json', encoding='utf8', mode='w')
json.dump(d1, f1)  # tutaj polskie znaki będą zepsute
f1.close()

dane = {
    'ksiazka': 'Dawca przysięgi',
    'film_na_wieczor': 'malaga',
    'coins': [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5]
}
f2 = open('../../files_sources/jsonout2.json', encoding='utf8', mode='w')
json.dump(dane, f2, ensure_ascii=False)  # ensure_ascii=False  - umożliwia zapis polskich znaków
f2.close()
