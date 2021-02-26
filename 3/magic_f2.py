from collections import Counter


class Account(dict):
    def __init__(self, **currencies):
        self.currencies = currencies

    def __len__(self):
        return len(self.currencies)

    def __repr__(self):
        return '{}({})'.format(
            self.__class__.__name__,
            ', '.join(f"{key}={val}" for key, val in self.currencies.items())
        )

    def __str__(self):
        return self.__class__.__name__ + ' with currencies: ' + str(self.currencies)

    def __add__(self, other):
        return dict(Counter(self.currencies) + Counter(other.currencies))

    def __iadd__(self, other):
        if isinstance(other, dict) or isinstance(other, Account):
            for s_key, s_val in self.items():
                for o_key, o_val in other.items():
                    if s_key == o_key:
                        self.currencies[s_key] += other[s_key]
        else:
            for key, val in self.currencies.items():
                self.currencies[key] += other
        return self

    def __mul__(self, other):
        return dict().update(sk: sv * ov for sk, sv, ok, ov in self, other)

    def __setitem__(self, key, value):
        super().__setitem__(key, value)

    def __contains__(self, item):
        return True if self.currencies.__contains__(item) else False

    def __delitem__(self, key):
        del self[key]


acc_1: Account = Account(eur=5, pln=2.3)
acc_2: Account = Account(eur=1, pln=1)

print('\nacc_1 =\n', acc_1)
print('acc_2 =\n', acc_2)

print('\nacc_1.__repr__() =\n', acc_1.__repr__())
print('repr(acc_2) =\n', repr(acc_2))

print('acc_1 + acc_2 =\n', acc_1 + acc_2)

print(id(acc_1))
print(acc_1)

acc_1 += {'eur': 10}
print(id(acc_1))
print(acc_1)

acc_1 += acc_2
print(id(acc_1))
print(acc_1)

print(acc_1.__contains__('eur'))

acc_1['eur'] = -2
print(acc_1['eur'])

print(acc_1 == dict(acc_1))

print(acc_1)
print(acc_2)
print(acc_1 * acc_2)