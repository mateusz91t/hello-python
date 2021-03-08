import py_20test_param as tp2


def test_podepnij_baze():
    bazy = ['Oracle', 'PostgreSQL', 'MS SQL', 'MySQL']
    for b in bazy:
        tp2.podepnij_baze(b)
        assert tp2.wykonaj_zapytanie() == 'ok'
    pass

# python -m pytest -k podepnij -v -W ignore::Warning
