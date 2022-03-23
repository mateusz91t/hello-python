import matplotlib.pyplot as plt
from random import random


# 1 linia
y = list(random() * 100 for e in range(100))
print(y)
plt.plot(y)
# plt.show()

# 2 linie
plt.close()
y = list(random() * 100 for _ in range(10))
z = list(random() * 100 for _ in range(10))
plt.plot(y)
plt.plot(z)
# plt.show()

# 2 linie z legendą
plt.close()
y = list(random() * 100 for _ in range(10))
z = list(random() * 100 for _ in range(10))
plt.plot(y, label='Seria y')
plt.plot(z, label='Seria z')
plt.legend()
# plt.show()

# 2 linie z legendą i nazwanymi osiami
plt.close()
y = list(random()*100 for _ in range(10))
plt.plot(y, label='Seria y')
plt.xlabel('oś __x')
plt.ylabel('oś y')
plt.legend()
# plt.show()

# 3 linie, kolorowanie ich, różne style i siatka
plt.close()
a = list(random()*100 for _ in range(10))
b = list(random()*100 for _ in range(10))
c = list(random()*100 for _ in range(10))
plt.plot(a, 'b-', label='Seria a')
plt.plot(b, 'r--', label='Seria b')
plt.plot(c, 'g:', label='Seria c')
plt.legend()
plt.grid()
# plt.show()

# inny kolor z hexa
plt.close()
a = list(random()*100 for _ in range(10))
plt.plot(a, '#FFAA00')
# plt.show()

# hex w nazwanym argumencie i wybranym stylem linii i zapis do pliku
plt.close()
a = list(random()*100 for _ in range(10))
plt.plot(a, '--', color='#FFAABB')
plt.savefig('wykres.png')
plt.show()

