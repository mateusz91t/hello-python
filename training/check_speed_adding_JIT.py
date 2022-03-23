import time
from numba import jit  # , njit

start = time.time()


@jit()
def do_something():
    n = 0
    for i in range(10_000_000):
        n += i


do_something()

print((time.time() - start))
