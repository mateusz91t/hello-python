import time
import threading


def odliczaj(nazwa_watku, ile):
    for x in range(ile):
        print(x)
        time.sleep(1)


f = threading.Thread(target=odliczaj, args=('pierwszy', 10), daemon=True)
f.start()
f.join()
