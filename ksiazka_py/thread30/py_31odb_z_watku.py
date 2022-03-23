import time
import concurrent.futures as cf


def oddaj():
    time.sleep(3)
    return 'koza'


wykonawca = cf.ThreadPoolExecutor()
zadanie = wykonawca.submit(oddaj)
zwrot = zadanie.result()
print(zwrot)
