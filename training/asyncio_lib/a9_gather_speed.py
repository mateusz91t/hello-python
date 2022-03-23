# todo 1: https://docs.python.org/3/library/asyncio-task.html#asyncio.Task.result
# todo 2: 4.4 https://render.githubusercontent.com/view/ipynb?color_mode=auto&commit=6275ca2b48e445adf8a3c4a8edccaf074e9e6aa9&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f64616674636f64652f6461667461636164656d792d707974686f6e5f6c6576656c75702d737072696e67323032312f363237356361326234386534343561646638613363346138656463636166303734653965366161392f365f415f6a616b5f6173796e63696f2f415f6a616b5f6173796e63696f2e6970796e62&nwo=daftcode%2Fdaftacademy-python_levelup-spring2021&path=6_A_jak_asyncio%2FA_jak_asyncio.ipynb&repository_id=355473955&repository_type=Repository#4.4-wykonanie-sekwencyjne-vs-asyncio-vs-w%C4%85tki
import asyncio
import datetime
import time

start = time.time()


async def bla_nb(coro_id):
    print(f'{datetime.datetime.now()} {coro_id}: before sleep')
    await asyncio.sleep(0.0001)
    print(f'{datetime.datetime.now()} {coro_id}: after sleep')


# it works simultaneously; gather [zbierać]
async def main3():
    await asyncio.gather(bla_nb(1), bla_nb(2))

for i in range(100):
    asyncio.run(main3())

print(f'Ended in {time.time() - start}')
