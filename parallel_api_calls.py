import asyncio
import aiohttp
import time

urls = [
    "https://dummyjson.com/users/1",
    "https://dummyjson.com/users/2",
    "https://dummyjson.com/users/3"
]

async def fetch(session, url):
    async with session.get(url) as response:
        data = await response.json()
        print(f"User ID: {data['id']}, Name: {data['firstName']}")

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        await asyncio.gather(*tasks)

start_time = time.time()
asyncio.run(main())
end_time = time.time()

print("Total Time Taken (Parallel):", end_time - start_time, "seconds")
