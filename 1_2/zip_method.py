list_1: list = list(range(0, 10, 2))
list_2: list = list(chr(x) for x in range(ord('a'), ord('a') + 10))

print(list_1)
print(list_2)

print(
    '\ntuples from two lists: list(zip(list_1,list_2)) =\n',
    list(zip(list_1, list_2))
)
print(
    'list&range: list(zip(list_2, range(10))) =\n',
    list(zip(list_2, range(10)))
)