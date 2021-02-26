def foo1(a: int = 1, b: int = 2, **kwargs: int):
    print(f'{type(a)}\ta = {a}')
    print(f'{type(b)}\tb = {b}')
    print(f'{type(kwargs)}\tkwargs = {kwargs}')
    print(f'{type(kwargs.keys())}\tkwargs.values() = {kwargs.keys()}')
    print(f'{type(kwargs.values())}\tkwargs.values() = {kwargs.values()}')
    return a + b + sum(kwargs.values())


def foo2(a: int = 1, b: int = 2, *c: int):
    print(f'{type(a)}\ta = {a}')
    print(f'{type(b)}\tb = {b}')
    print(f'{type(c)}\tc = {c}')
    return a + b + sum(c)


def foo3(*, a: int = 1, b: int = 3, **kwargs: int):  # * - U have to get named args only
    print(f'{type(a)}\ta = {a}')
    print(f'{type(b)}\tb = {b}')
    print(f'{type(kwargs)}\tkwargs = {kwargs}')
    print(f'{type(kwargs.keys())}\tkwargs.values() = {kwargs.keys()}')
    print(f'{type(kwargs.values())}\tkwargs.values() = {kwargs.values()}')
    return a + b + sum(kwargs.values())


print(foo1(a=10, e=100, f=1))

print(foo2(1, 2, 3, 20))

print(foo3(a=1, e=2, f=3))
