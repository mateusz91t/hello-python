import random as r
from decimal import Decimal

list_1: list = list(range(20))


print(
    'list_1) =\n',
    list_1)

r.shuffle(list_1)
print(
    'after: r.shuffle(list_1)',
    list_1
)

print(
    'r.random() =\n',
    r.random()
)

print(
    'r.choice(list_1) =\n',
    r.choice(list_1)
)

print(
    '0.1 + 0.1 + 0.1 =\n',
    0.1 + 0.1 + 0.1,
    "\nDecimal('0.1') + Decimal('0.1') + Decimal('0.1') =\n",
    Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
)
