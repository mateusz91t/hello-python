
def __foo_bar__(a, b={"a": 1}, c=[1, 2, 3]):
    pass


def _foo_bar_(*, x=1, y=2, z=3):
    pass


# to nie działa
# def FooBar(a, b=1, c=None, **kwargs, *args):
#     pass


def foo_bar(a, b, c):
    pass


class FooBar_baz10(10):
    pass


class BarBar(int):
    pass


class Foo_baz(object):
    pass


class bar_baz():
    pass
