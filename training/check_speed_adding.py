import time

start = time.time()


def do_something():
    n = 0
    for i in range(10_000_000):
        n += i


do_something()

print((time.time() - start))
