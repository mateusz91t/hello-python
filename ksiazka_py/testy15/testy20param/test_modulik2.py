import py_20test_param as tp2
import pytest

dbs = ['Oracle', 'PostgreSQL', 'MS SQL', 'MySQL']


@pytest.mark.parametrize('baza', dbs)
def test_podepnij_baze(baza):
    tp2.podepnij_baze(baza)
    print(f'baza: {baza}')
    assert tp2.wykonaj_zapytanie() == 'ok'

# python -m pytest -k podepnij -v -W ignore::Warning
