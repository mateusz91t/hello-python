podpieta_baza = None


def podepnij_baze(nazwa):
    global podpieta_baza
    podpieta_baza = nazwa


def wykonaj_zapytanie():
    global podpieta_baza
    print(f'{podpieta_baza}: select * from prod')
    if podpieta_baza == 'MS SQL':
        raise Exception('FUUUUUUUUUU')
    return 'ok'
