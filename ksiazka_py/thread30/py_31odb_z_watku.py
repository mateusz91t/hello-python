import time
import concurrent.futures


def oddaj():
    time.sleep(3)
    return 'koza'


wykonawca = concurrent.futures.ThreadPoolExecutor()
zadanie = wykonawca.submit(oddaj)
zwrot = zadanie.result()
print(zwrot)
