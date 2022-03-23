# list, set comprehensions
# listy składane lub wyrażenia listowe

list_1: list = list(x for x in range(10) if x % 2 == 0)

print(
    'list_1 =\n',
    list_1
)

set_1: set = set(x for x in [1, 1, 2, 2, 3])

print(
    'set_1 =\n',
    set_1
)

tuple_1: tuple = tuple(x for x in [1, 1, 2, 2, 3])

print(
    'tuple_1 =\n',
    tuple_1
)

generator_1 = (x for x in range(5))

print(
    'type(generator_1) =\n',
    type(generator_1),
    'generator_1 =\n',
    generator_1
)

next(generator_1)
