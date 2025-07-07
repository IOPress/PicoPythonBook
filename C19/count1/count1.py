import uasyncio

async def count():
    global myCounter
    for i in range(1000):
        temp = myCounter+1
        await uasyncio.sleep(0)
        myCounter = temp

async def main():
    await uasyncio.gather(count(),count())
    print(myCounter)

myCounter=0
uasyncio.run(main())