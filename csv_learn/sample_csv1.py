import csv
from collections import Counter


with open('airtravel.csv') as travels_file:
    travels_reader = csv.DictReader(travels_file)
    lz1 = list(zip(*list(dct for dct in travels_reader)))

# for tupl in lz1:
#     print(tupl)

print(
    Counter(lz1[0])
)




cz1 = list(Counter(tupl) for tupl in lz1)

print(cz1)
