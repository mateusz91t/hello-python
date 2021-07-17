import asyncio
import datetime
import requests
import threading


async def bla(coro_id):
    print(f'{datetime.datetime.now()} {coro_id}: before sleep')
    await asyncio.sleep(2)
    print(f'{datetime.datetime.now()} {coro_id}: after sleep')