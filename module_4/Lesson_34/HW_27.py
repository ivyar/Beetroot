# 1
import threading
import time

def ping(duration):
    start = time.time()
    while time.time() - start < duration:
        print("Пінг")
        time.sleep(2)

def pong(duration):
    start = time.time()
    while time.time() - start < duration:
        print("Понг")
        time.sleep(1)

duration = 6

t1 = threading.Thread(target=ping, args=(duration,))
t2 = threading.Thread(target=pong, args=(duration,))

t1.start()
t2.start()

t1.join()
t2.join()

# 2
import asyncio

async def get_user(id):
    await asyncio.sleep(1)
    print(f"User {id}")

async def get_weather(city):
    await asyncio.sleep(2)
    print(f"Weather in {city}")

async def get_news():
    await asyncio.sleep(1)
    print("News")

async def main():
    print(f'started at {time.strftime("%X")}')
    await asyncio.gather(
        get_user(1),
        get_weather("Kyiv"),
        get_news()
    )
    print(f'finished at {time.strftime("%X")}')

asyncio.run(main())