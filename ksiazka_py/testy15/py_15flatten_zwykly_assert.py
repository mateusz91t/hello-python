from ksiazka_py.testy15.py_15flatten import flatten

assert flatten([1, 2, 3]) == [1, 2, 3]
assert flatten([]) == []
assert flatten([1, [2, 3], 4]) == [1, 2, 3, 4]
assert flatten([1, [2, 3], 4]) != [1, [2, 3], 4]
assert flatten([[1, 2, [3, 4, 5], [6], 7, 8], 9]) == [*range(1, 10)]
