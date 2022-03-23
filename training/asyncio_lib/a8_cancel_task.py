import asyncio
import datetime
import requests
import threading


async def bla(coro_id):
    print(f'{datetime.datetime.now()} {coro_id}: before try')
    try:
        await asyncio.sleep(5)
    # after e.g. User exited the app it is possible to clean up, mark not processed data and more
    # to do this we need to catch CancelledError
    except asyncio.CancelledError:
        print(f'{datetime.datetime.now()} {coro_id}: catch CancelledError')
        # ... clean up code
    else:
        print(f'{datetime.datetime.now()} {coro_id}: else')
    finally:
        print(f'{datetime.datetime.now()} {coro_id}: finally')

async def main1():
    task_1 = await asyncio.create_task(bla(1))
    print(task_1.get_stack())
    await asyncio.sleep(2)
    print(f'{datetime.datetime.now()}: Cancel task_1')
    task_1.cancel()
    print(f'{datetime.datetime.now()}: Canceled task_1')


asyncio.run(main1())
