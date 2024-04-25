#!/usr/bin/env python3
import asyncio
import random


async def async_generator():
    """
    Coroutine that loops 10 times, asynchronously waits for 1 second each time,
    and yields a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def main():
    async for num in async_generator():
        print(num)

asyncio.run(main())
