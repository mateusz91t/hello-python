# podejście bez dekoratora
print('podejście bez dekoratora:')


def bazowa():
    print('bazowa()')


def dekor1(funkcja):
    print('dekor1()')

    def opatulajaca():
        print('opatulajaca()')
        funkcja()

    return opatulajaca


d1 = dekor1(bazowa)
d1()

# podejście z dekoratorem
print('\npodejście z dekoratorem:')


def dekor2(funkcja):
    print('dekor2()')

    def wew():
        print('dekor2().wew()')
        funkcja()

    return wew


@dekor2
def bazowa2():
    print('bazowa2()')


bazowa2()

# dekorowanie z parametrami
print('\ndekorowanie z parametrami:')


def dekor3(funkcja):
    print('dekor3()')

    def wew(x):
        print('dekor3().wew()')
        print('elo1')
        x = x.upper()
        funkcja(x)
        print('elo3')

    return wew


@dekor3
def bazowa3(x):
    print(f'siemanko {x}')


bazowa3('Janek')


def dekor4(funkcja, **kwargs):
    """dokumentacja tralala dekor4(funkcja, **kwargs)"""
    def wew(**kwargsa):
        for x in kwargsa:
            kwargsa[x] = kwargsa[x].upper()
        funkcja(**kwargsa)

    return wew


@dekor4
def bazowa4(**kwargs):
    """dokumentacja tralala bazowa4(**kwargs)"""
    for k in kwargs:
        print(k, kwargs[k])


bazowa4(a='abc', b='bcd', c='cde')
print(help(bazowa4))
