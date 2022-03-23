import pytest

import py_21niby_baza as nb


# autouse zadziała tak tak setup_module - nie trzeba podawać nazwy funkcji w parametrach testów
@pytest.fixture(scope="module", autouse=True)
def load_stuff():
    print("\n", "#" * 10, " load ", "#" * 10)
    nb.load_db()


def test_get_data():
    assert len(nb.get_data()) > 0
    print("\ntest_get_data")


def test_get_one():
    assert nb.get_one(0)[1] == "Marian"
    print("\ntest_get_one")
