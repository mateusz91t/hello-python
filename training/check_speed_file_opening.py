import time

start = time.time()

for _ in range(100000):
    fo = open('files_sources/tekst.txt', encoding='utf-8')
    fo.close()

print((time.time() - start) * 1000)
