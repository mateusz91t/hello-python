from collections import Counter


class Account:
    def __init__(self, **currencies):
        self.currencies = currencies

    def __len__(self):
        return len(self.currencies)

    def __add__(self, other):
        d_1 = Counter(self.currencies) + Counter(other.currencies)
        return Account(**dict(d_1))

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join((str(x[0]) + '=' + str(x[1])) for x in self.currencies.items())})"

    def __str__(self):
        return f"{self.__dict__}"


acc_1: Account = Account(eur=5, pln=2.3)
print(
    'acc_1.__repr__() =\n',
    acc_1.__repr__()
)
acc_2: Account = Account(eur=1, pln=1)
print(
    'acc_2.__repr__() =\n',
    acc_2.__repr__()
)

print('\nacc_1 =\n', acc_1)
print('acc_2 =\n', acc_2)
acc_3 = acc_1 + acc_2

print('acc_3 =\n', acc_3)
