import sys
import time
import threading


def odliczaj(nazwa_watku, ile):
    for x in range(ile):
        print(f'{x}: {nazwa_watku}\t')
        time.sleep(1)


f = threading.Thread(target=odliczaj, args=('second', 5))
f.start()
odliczaj('main', 5)
f.join()

print(sys.version)
