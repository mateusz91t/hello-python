import httpx  # it support async and sequential run
import time

import requests


def call_httpbin1(delay):
    response = httpx.get(f'https://httpbin.org/delay/{delay}')
    return response.status_code


def main1():
    start = time.time()
    responses = [call_httpbin1(1), call_httpbin1(2), call_httpbin1(3), call_httpbin1(4)]
    print(f'sequential:\t\tReceived {len(responses)} in {time.time() - start}')


main1()


import asyncio


async def call_httpbin2(delay):
    async with httpx.AsyncClient() as client:
        response = await client.get(f'https://httpbin.org/delay/{delay}')
        return response.status_code


async def main2():
    start = time.time()
    responses = await asyncio.gather(call_httpbin2(1), call_httpbin2(2), call_httpbin2(3), call_httpbin2(4))
    print(f'httpx.AsyncClient:\tReceived {len(responses)} in {time.time() - start}')


asyncio.run(main2())


import threading
import requests


responses_lock = threading.Lock()


def call_httpbin3(responses, delay):
    response = requests.get(f'https://httpbin.org/delay/{delay}')
    responses_lock.acquire()
    responses.append(response.status_code)
    responses_lock.release()


def main3():
    start, responses, call_threads = time.time(), list(), list()
    for i in range(1, 5):
        call_thread = threading.Thread(target=call_httpbin3, args=(responses, i))
        call_threads.append(call_thread)
        call_thread.start()
    for i in call_threads:
        i.join()
    print(f'threading.Thread:\tReceived {len(responses)} in {time.time() - start}')


main3()


# output
# sequential:             Received 4 in 12.29050612449646
# httpx.AsyncClient:      Received 4 in 4.713970899581909
# threading.Thread:       Received 4 in 4.695679426193237

# asyncio gets less resources than threading.
# Coroutines from asyncio are fragments of an app. 
# In aio all asynchronous tasks run in 1 coroutine that runs in only 1 thread that runs in only 1 process.
# Threads from threading make calls to OS kernel to make new Thread.

# maybe if we waste CPU time during we wait for something better is asyncio
# but if we want more power we should use Thread?

# concurrency (asyncio, threading) > parallelism (multiprocessing)