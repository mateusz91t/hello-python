y = lambda x: x + 1  # not recommended

print('y(1) =\n', y(1))

print(
    '(lambda __x: __x + 1)(10) =\n',
    (lambda x: x + 1)(10)
)

list_1: list = list(range(10))

print('list_1 =\n', list_1)

print(
    'list(map(lambda __x: __x + 1, list_1)) =\n',
    list(map(lambda x: x + 1, list_1))
)

print(
    'list(filter(lambda __x: __x % 3 == 0, list_1)) =\n',
    list(filter(lambda x: x % 3 == 0, list_1))
)
