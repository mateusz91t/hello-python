from concurrent.futures import ThreadPoolExecutor
import datetime
import time


def count_and_return(which_thread:str, n: int):
    for i in range(n):
        print(f'{i}: {which_thread}...')
        time.sleep(1)
    return f'{which_thread} ended in {n} seconds: {str(datetime.datetime.now())}'

print('create a worker:')
worker = ThreadPoolExecutor()
print('create a task:')
task = worker.submit(count_and_return, 'second', 5)
print('return a result:')

# start task in main thread
print(count_and_return('main', 5))
# get output from another thread
res = task.result()
print(res)
