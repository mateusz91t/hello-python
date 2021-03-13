from datetime import date
from datetime import timedelta


def tommorow() -> date:
    return date.today() + timedelta(days=1)


def tommorow2(from_date: date) -> date:
    return from_date + timedelta(days=1)


print(tommorow())
print(tommorow2(date(2021, 3, 13)))
