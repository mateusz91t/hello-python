# import datetime
import asyncio
import datetime


async def bla():
    print(f'{datetime.datetime.now()}: before sleep')
    await asyncio.sleep(2)
    print(f'{datetime.datetime.now()}: after sleep')


# good practice to contain more func in 1 coroutine
async def main():
    await bla()


bla()
# await main()  # doesn't work in a .py file but in .ipynb file works

# to run in .py file it needs:
asyncio.run(main())

# returns:
# 2021-07-17 17:52:12.254356: before sleep
# 2021-07-17 17:52:14.255308: after sleep


# but how to run simultaneously [simiulte^nesli:jednocześnie]
async def bla_nb(coro_id):
    print(f'{datetime.datetime.now()} {coro_id}: before sleep')
    await asyncio.sleep(2)
    print(f'{datetime.datetime.now()} {coro_id}: after sleep')


# it works sequentially!
async def main2():
    await bla_nb(1)
    await bla_nb(2)

# why it works sequentially?
# Key word `await` stops the main enentloop. It says: Wait! We need the result from that method!
# `await` forces \wymusza\ the stopping of an main method that contains an awaited method


asyncio.run(main2())

# it works simultaneously; gather [zbierać]
async def main3():
    await asyncio.gather(bla_nb(1), bla_nb(2))


asyncio.run(main3())
