baza = list()


def load_db():
    print('#' * 10, ' ŁADOWANIE BAZY ', '#' * 10)
    global baza
    baza = [
        (1, 'Marian'),
        (2, 'Czesław'),
        (3, 'Zenon'),
        (4, 'Florian'),
    ]


def get_data():
    global baza
    return baza


def get_one(index):
    global baza
    return baza[index]
