from datetime import datetime
from typing import Callable, Tuple

fake_start = datetime(2020, 1, 1, 18, 0, 0)
fake_end = datetime(2020, 1, 1, 18, 3, 15)


def go3(now: Callable[[], datetime], ) -> Tuple[datetime, datetime]:
    started_at = now()
    for x in range(2 ** 22):
        y = x + x
    ended_at = now()
    return started_at, ended_at


# print(go3(datetime.now))

gen = iter([fake_start, fake_end])
# print(go3(lambda: next(gen)))

gen2 = iter(['ciach chach', 'prach prach'])
# print((go3(lambda: next(gen2))))


