import time
import httpx


def call_httpbin(delay):
    response = httpx.get('https://httpbin.org/delay/' + str(delay))
    return response.status_code

start = time.time()

for i in range(4):
    print(call_httpbin(i))

print('Finished in %s s' % (round(time.time() - start, 3)))
