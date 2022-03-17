from datetime import datetime
import time
from functools import lru_cache


# #1
def czekaj():
    time.sleep(1)
    return 1


poczatek = datetime.now()
for _ in range(5):
    czekaj()
koniec = datetime.now()
print(koniec-poczatek)  # 0:00:10.004003


# #2
@lru_cache(maxsize=None)
def czekaj2():
    time.sleep(1)
    return 1


poczatek2 = datetime.now()
for _ in range(5):
    czekaj2()
koniec2 = datetime.now()
print(koniec2-poczatek2)  # 0:00:01.000001
