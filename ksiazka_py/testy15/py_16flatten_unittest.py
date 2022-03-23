import unittest
from ksiazka_py.testy15.py_15flatten import flatten


class TestsFlatten(unittest.TestCase):
    def test_flatten_not_nested_list(self):
        test_list = [1, 2, 3]
        result = flatten(test_list)
        assert result

    def test_flatten_nested_list(self):
        test_list = [1, [2, 3], 4]
        result = flatten(test_list)
        assert result == [1, 2, 3, 4]

    def test_flatten_empty_list(self):
        test_list = []
        result = flatten(test_list)
        assert result == []

    def test_flatten_different_nestings(self):
        test_list = [[1, 2, [3, 4, 5], [6], 7, 8], 9]
        result = flatten(test_list)
        assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9]

if __name__ == '__main__':
    unittest.main()