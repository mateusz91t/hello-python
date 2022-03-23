import pytest

import py_21niby_baza as nb


# uruchomi load_stuff() jeden raz przed uruchomieniem testów z nazwą tej f. w definicji parametrów
@pytest.fixture(scope="module")
def load_stuff():
    print("\n", "#" * 10, " load ", "#" * 10)
    nb.load_db()


def test_get_data(load_stuff):
    assert len(nb.get_data()) > 0
    print("\ntest_get_data")


def test_get_one(load_stuff):
    assert nb.get_one(0)[1] == "Marian"
    print("\ntest_get_one")


def teardown_module():
    print(
        "\n",
        "#" * 10,
        ' bye from `teardown_module` in `pytest.fixture(scope="module")` ',
        "#" * 10,
    )
