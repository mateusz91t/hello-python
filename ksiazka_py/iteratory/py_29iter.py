class IncrementIterator:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == self.i:
            raise StopIteration
        self.i += 1
        return self.i


class NieskonczonyIterator:
    x = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.x += 1
        return self.x


for e in IncrementIterator(3):
    print(e)
ie = IncrementIterator(4)

print()
for x in range(4):
    print(next(ie))

print()
ni = NieskonczonyIterator()
for x in range(3):
    print(next(ni))
