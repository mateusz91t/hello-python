import py_21niby_baza as nb


# muszę pobierać KAŻDORAZOWO do każdej metody dane z bazy
def test_get_data():
    nb.load_db()
    assert len(nb.get_data()) > 0


def test_get_one():
    nb.load_db()
    assert nb.get_one(0)[1] == 'Marian'
