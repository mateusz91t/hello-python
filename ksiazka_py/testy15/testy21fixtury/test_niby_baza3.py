import py_21niby_baza as nb
import pytest


# to znów powoduje uruchamianie dla każdej funkcji z parametrem nazwy dekorowanej funkcji
@pytest.fixture
def load_stuff():
    print('\n', '#' * 10, ' load ', '#' * 10)
    nb.load_db()


def test_get_data(load_stuff):
    assert len(nb.get_data()) > 0


def test_get_one(load_stuff):
    assert nb.get_one(0)[1] == 'Marian'
