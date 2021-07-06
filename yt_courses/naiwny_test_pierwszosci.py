import math


def test_pierwszosci(x: int) -> bool:
    if x <= 1:
        return False
    # for i in range(2, x):
    # for i in range(2, int(x/2)):  # We don't have to check all numbers, a half is enough
    # math.sqrt(16) == 16 ** 0.5
    for i in range(2, int(x ** .5)):  # we should check only a square root [pierwiastek kwadratowy]
        if x % i != 0:
            continue
        else:
            return False
    return True
