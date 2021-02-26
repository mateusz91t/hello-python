from collections import Counter
import csv
import re
import operator as op


"""
Wprowadzenie:

Jesteś pracownikiem w firmie spedycyjnej "TEU Logistics".
Twoja firma zajmuje się przewozem towarów w morskich kontenerach własnymi statkami po całym świecie.
Manager poprosił Cię o małą analizę danych dlatego wysłał Ci plik z danymi (CSV) w którym są dane aktualnie transportowanych kontenerów przez "TEU Logistics".
Dane są trochę mało czytelne i jest ich za dużo na "ręczne" kalkulacje.

W pierwszym wierszu, w każdej kolumnie podany jest numer, nazwa i klasa statku który przewozi ładunek.
W kolejnych wierszach w każdej kolumnie widnieją dane kontenerów znajdującego się na pokładzie danego statu w kolumnie wraz z kwotą jaka została pobrana za przewóz kontenera.

Szczegóły

Statek:

Nazwa statku, jego port startowy oraz docelowy i klasa podana jest w formacie:

    aa-bb: xxxxxx (ttttttt)

gdzie:

    aa - kraj załadunku statku
    bb - kraj rozładunku statku
    xxxxxx: nazwa statku
    tttttt: klasa statku

np: ES-PL: Cool Ship (Small Feeder)

Kontener:

Każdy kontener ma identyfikator nadany w formacie:

    aa-bb-cccccccc/yyyy/xx@ddddddddd.ee

gdzie:

    aa - kraj pochodzenia kontenera
    bb - kraj docelowy kontenera
    ccccccccc - numer kontenera (nie jest unikalny !!)
    yyyy - waga kontenera w kilogramach (cyfrowo 0001-9999)
    xx - typ ładunku w kontenerze (A0-Z9)
    dddddddd.ee - nazwa i kraj pochodzenia firmy która nadaje kontener, kraj jest 2 literowym oznaczeniem wg ISO 3166-1
    długość pól cccccc, dddddd nie jest stała
    pl-jp-2343432/2201/A1@companyname.pl oraz pl-jp-1223123/2201/A1@companyname.de to kontenery 2 różnych firm wg systemu informatycznego Twojej firmy.

Rekord jest połączeniem identyfikatora i kwoty w formacie:

    identyfikator/kwota:
        pl-jp-2343432/3100/Z1@companyname.pl/83427

Z wszelakich powodów takich jak różne kontrakty, terminy, kolejność załadunku, waga i rodzaj ładunku, cena wysyłki kontenera jest bardzo różna.
Zauważ że kraj pochodzenia i destynacji kontenera nie jest tożsamy z portem docelowym dla kontenera, często taki kontenery trzeba przeładować kilka razy.

Zadanie rekrutacyjne 1:
(15pkt) Ile kontenerów finalnie trafi do Japonii (JP)? (liczba kontenerów)

Zadanie rekrutacyjne 2:
(15pkt) Jaka klasa statku średnio przewozi najwięcej kontenerów? (sama nazwa klasy statku)

Zadanie rekrutacyjne 3:
(20pkt) Jaka jest średnia waga kontenera z przetworami owocowymi (A3) z dokładnością do 1 kg np: 1234 (zaokrąglane w górę)?

Zadanie rekrutacyjne 4:
(25pkt) Która Polska firma globalnie przewozi najwięcej kontenerów? (nazwa firmy)

Zadanie rekrutacyjne 5:
(25pkt) Jakiego typu ładunek o największej wartości eksportują Niemieckie firmy z Niemczech? (wartość to stosunek ceny do wagi)
"""

with open('../../dane.csv') as file:
    whole_file = file.read()
    file.seek(0)
    ships = file.readline()
    containers = file.read()
    file.seek(0)
    reader = list(csv.reader(file, delimiter=';'))
    transpose_reader = [list(filter(lambda container: container != '', tupl)) for tupl in zip(*reader)]

ships = ships.split(';')
ship_pattern = r'([A-Z]{2})-([A-Z]{2})-(\d*)/(\d{4})/(\w{2})@(\w*)\.([a-z]{2})/(\d*)[;|\n]?'
all_containers = re.findall(ship_pattern, containers)

# z1
z1 = Counter(destination[1] for destination in all_containers)
print(z1['JP'])

# z2
z2 = {contains[0]: len(contains) - 1 for contains in transpose_reader}

type_ship_pattern = r'.*\((.*)\)'
containers_on_ships = [(re.sub(type_ship_pattern, r'\1', k), v) for k, v in z2.items()]
containers_on_type_ships = dict()
for tupl in containers_on_ships:
    if tupl[0] in containers_on_type_ships.keys():
        containers_on_type_ships[tupl[0]].append(tupl[1])
    else:
        containers_on_type_ships[tupl[0]] = [tupl[1]]

the_highest_type = containers_on_type_ships.copy()

for key in containers_on_type_ships.keys():
    the_highest_type[key] = sum(the_highest_type[key])/len(the_highest_type[key])

print(max(the_highest_type.items()))

# z3
contains_a3 = [int(tupl[3]) for tupl in all_containers if tupl[4] == 'A3']
avg_a3 = sum(contains_a3)/len(contains_a3)
if avg_a3 == round(avg_a3):
    a3 = avg_a3
else:
    a3 = round(avg_a3) + 1
print(a3)

# z4
contains_pl = [tupl[5] for tupl in all_containers if tupl[6] == 'pl']
print(Counter(contains_pl))

# z5
contains_de_de = [(tupl[4], int(tupl[-1]) / int(tupl[3])) for tupl in all_containers if tupl[6] == 'de' and tupl[0] == 'DE']
print(list(reversed(sorted(contains_de_de, key=op.itemgetter(1)))))
print(max(contains_de_de, key=op.itemgetter(1)))
