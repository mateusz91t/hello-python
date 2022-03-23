def bmi(m, w):
    if w < 0.5 or w > 2.5:
        raise Exception
    return round(m / w ** 2, 2)


print(bmi(75, 1.76))
# print(bmi(75, 0.4))  # wywali się i nie powie co nie tak: samo Exception


def bmi2(m, w):
    if w < 0.5 or w > 2.5:
        raise Exception("Wzrost poza zakresem")
    return round(m / w ** 2, 2)


print(bmi2(75, 1.76))
# print(bmi2(75, 0.4))  # wywali się z info


class HeightOutOfRangeException(Exception):
    def __init__(self):
        super().__init__('Wzrost jest mniejszy niż 0.5 lub większy niż 2.5')


def bmi3(m, w):
    if w < 0.5 or w > 2.5:
        raise HeightOutOfRangeException
    return round(m / w ** 2, 2)


print(bmi3(75, 1.76))
# print(bmi3(75, 0.4))  # wywali się z info z klasy - można reużywać teraz tej klasy


# a teraz z podanym parametrem błędu
class HeightOutOfRangeException2(Exception):
    def __init__(self, w):
        super().__init__(f"Wzrost {w} jest za mały lub za duży")


def bmi4(m, w):
    if w < 0.5 or w > 2.5:
        raise HeightOutOfRangeException2(w)
    return round(m / w ** 2, 2)


print(bmi4(75, 0.4))  # z przekazaniem parametru
