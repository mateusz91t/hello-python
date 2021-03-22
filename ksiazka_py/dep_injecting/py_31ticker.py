import datetime
from typing import Iterator
from py_30di import go3


def ticker(
        start: datetime.datetime,
        interval: datetime.timedelta
) -> Iterator[datetime.datetime]:
    """Generate an uneding stream of datetimes in fixed intervals

    Useful to test processes which require datetime for each step."""
    current = start
    while True:
        yield current
        current += interval


gen = ticker(datetime.datetime(2020, 1, 1, 15, 0, 0), datetime.timedelta(seconds=20))
print(go3(lambda: next(gen)))
print(go3(lambda: next(gen)))
print(go3(lambda: next(gen)))
