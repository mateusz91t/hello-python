import requests
import threading
import time

responses_lock = threading.Lock()

def call_httpbin_async(responses, delay):
    response = requests.get(f'https://httpbin.org/delay/{delay}')
    responses_lock.acquire()
    responses.append(response.status_code)
    responses_lock.release()

start = time.time()
responses, call_threads = list(), list()

for i in range(4):
    call_thread = threading.Thread(target=call_httpbin_async,
        args=(responses, i))
    call_threads.append(call_thread)
    call_thread.start()

for element in call_threads:
    element.join()

print(f'Received {responses} in {round(time.time() - start, 3)}s')
