import sys
import time
import threading


def slowly(name: str):
    print(f'{name} thread started')
    time.sleep(1)
    print(f'{name} thread stopped')


x = threading.Thread(target=slowly, args=('second',))
x.start()
slowly('main')

print(sys.version)
