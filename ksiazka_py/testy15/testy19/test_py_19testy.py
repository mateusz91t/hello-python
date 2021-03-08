import pytest
import py_19testy as p19t


@pytest.mark.podstawowe
def test_sumuj():
    assert p19t.sumuj(5, 3) == 8


@pytest.mark.szczegolowe
def test_daj_cyfry_min():
    tab = p19t.daj_cyfry()
    assert min(tab) == 1


@pytest.mark.szczegolowe
def test_daj_cyfry_max():
    tab = p19t.daj_cyfry()
    assert max(tab) == 10


@pytest.mark.podstawowe
def test_daj_cyfry_len():
    tab = p19t.daj_cyfry()
    assert len(tab) == 10
