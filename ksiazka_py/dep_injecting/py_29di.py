from datetime import datetime
from typing import Callable, Tuple
from unittest.mock import patch
from unittest import mock


def go() -> Tuple[datetime, datetime]:
    started_at = datetime.now()
    for x in range(2 ** 22):
        y = x + x
    ended_at = datetime.now()
    return started_at, ended_at


def now() -> datetime:
    return datetime.now()


def go2():
    started_at = now()
    for x in range(2 ** 22):
        y = x + x
    ended_at = now()
    return started_at, ended_at


print(go())
print(go2())

fake_start = datetime(2020, 1, 1, 18, 0, 0)
fake_end = datetime(2020, 1, 1, 18, 3, 15)


# with patch('__main__.now') as mpn:
#     mpn.
#     print(go2())


print('go3')


def go3(now: Callable[[], datetime]) -> Tuple[datetime, datetime]:
    started_at = now()
    for x in range(2 ** 22):
        y = x + x
    ended_at = now()
    return started_at, ended_at


print(go3(datetime.now))

gen = iter([fake_start, fake_end])
print(go3(lambda: next(gen)))
