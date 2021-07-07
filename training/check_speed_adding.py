import time

start = time.time()

n = 0

for i in range(1000000):
    n += i

print((time.time() - start) * 1000)
