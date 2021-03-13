import time
import threading


def czek(tekst):
    print(f'start wątku {tekst}')
    time.sleep(3)
    print(f'koniec wątku {tekst}')


x = threading.Thread(target=czek, args=('thread!!!!',))
x.start()
czek('MAIN!!!')
