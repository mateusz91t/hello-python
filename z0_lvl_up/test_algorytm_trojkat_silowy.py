import pytest
from z0_lvl_up.algorytm_trojkat_silowy import *

very_easy = ['D:/Mateusz/nauka/python/python_lvl_up/zad_rekr/1-very_easy.txt']


@pytest.mark.parametrize('plik', very_easy)
def test_get_data(plik):
    assert type(get_data(plik)) == list
    assert len(get_data(plik)) > 0


@pytest.mark.parametrize(
    'list_in, list_out',
    [
        [
            [[0], [0, 0]],
            [[0, 0], [0, 1], [0, 0, 0], [0, 0, 1]]
        ],
        [
            [[0, 1, 1], [0, 1, 1, 1, 1]],
            [[0, 1, 1, 1], [0, 1, 1, 2], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 2]]
        ]
    ]
)
def test_increase_paths(list_in, list_out):
    assert len(increase_paths(list_in)) == len(list_out)
