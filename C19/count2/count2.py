import uasyncio

async def count():
    global myCounter
    global myLock
    for i in range(1000):
        async with myLock:
            temp=myCounter+1
            await uasyncio.sleep(0)
            myCounter=temp

async def main():
    await uasyncio.gather(count(),count())
    print(myCounter)

myCounter=0
myLock=uasyncio.Lock()
uasyncio.run(main())