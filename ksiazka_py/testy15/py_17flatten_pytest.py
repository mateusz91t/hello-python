import pytest
from ksiazka_py.testy15.py_15flatten import flatten


@pytest.mark.parametrize(
    "param, result",
    [
        [[1, 2, 3], [1, 2, 3]],
        [[1, [2, 3], 4], [1, 2, 3, 4]],
        [[], []],
        [[[1, 2, [3, 4, 5], [6], 7, 8], 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]]
    ]
)
def test_value_comparator(param: list, result: list):
    assert flatten(param) == result
