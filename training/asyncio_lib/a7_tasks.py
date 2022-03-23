import datetime
import asyncio


async def bla(coro_id):
    print(f'{datetime.datetime.now()} {coro_id}: before sleep')
    await asyncio.sleep(2)
    print(f'{datetime.datetime.now()} {coro_id}: after sleep')


async def main1():
    print(f'{datetime.datetime.now()}: Started main1')
    task_1 = asyncio.create_task(bla(1))
    task_2 = asyncio.create_task(bla(2))
    # the awaiting is important to get both prints from bla() !
    # comment these next 2 lines and run to check it
    print(f'{datetime.datetime.now()}: Created tasks')
    await task_1 
    await task_2
    print(f'{datetime.datetime.now()}: Awaited tasks')


# Why doesn't it work well? :( bla() prints only 1st print.
# 
# edited:
# if I don't await task_1 and _2 i can get only 1st call of print
asyncio.run(main1())
