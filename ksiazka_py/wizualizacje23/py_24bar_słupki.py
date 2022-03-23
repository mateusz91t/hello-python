import matplotlib.pyplot as plt
from random import random
from calendar import month_name

# słupki z podziałem na miesiące
x = list(month_name[1:])
y = list(random() * 10000 for _ in range(12))
plt.bar(x, y)
# plt.show()

# kolorowanie słupków
plt.close()
x = list(month_name[1:])
y = list(random() * 10000 for _ in range(12))
wykres = plt.bar(x, y)
wykres[0].set_color('r')
print(type(wykres[0]), wykres[0])
# plt.show()

# kolorowanie wszystkich słupków i dodanie zielonej linii
plt.close()
x = list(month_name[1:])
y = list(random() * 10000 for _ in range(12))
z = list(random() * 10000 for _ in range(12))
wykres = plt.bar(x, y)
for _ in range(12):
    wykres[_].set_color('r')
print(type(wykres[0]), wykres[0])
plt.plot(z, 'g')
plt.show()
