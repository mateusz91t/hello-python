import py_21niby_baza as nb


def setup_module():
    print('\n', '#' * 10, ' setup ', '#' * 10)
    nb.load_db()


def teardown_module():
    print('\n', '#' * 10, ' bye ', '#' * 10)


def test_get_data():
    assert len(nb.get_data()) > 0


def test_get_one():
    assert nb.get_one(0)[1] == 'Marian'
