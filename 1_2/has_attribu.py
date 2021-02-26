def foo_1(a: int):
    b: int = 10
    return a * b


print(
    'foo_1(2) =\n',
    foo_1(2)
)

foo_1.c = -1
print(
    'foo_1.c =\n',
    foo_1.c
)

# doesn't work
# print(
#     'foo_1.b =\n',
#     foo_1.b
# )

foo_1.b = 3
z = foo_1.b
print(
    'z =\n',
    z
)
print(
    'foo_1(2) =\n',
    foo_1(2)
)

print(
    "\nhasattr(foo_1, 'b') =\n",
    hasattr(foo_1, 'b'),
    "\nhasattr(foo_1, 'a') =\n",
    hasattr(foo_1, 'a'),
    "\nhasattr(foo_1, 'c') =\n",
    hasattr(foo_1, 'c')
)

print(
    'vars(foo_1) =\n',
    vars(foo_1)
)
