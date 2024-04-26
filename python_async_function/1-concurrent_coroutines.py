#!/usr/bin/env python3
""" async routine called wait_n that takes in 2
int arguments (in this order"""
import asyncio
import random
from typing import List


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay seconds and returns it.

    Args:
        max_delay (int, optional): The maximum delay in seconds (default is 10).

    Returns:
        float: The random delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns wait_random
    n times with the specified max_delay
    and returns the list of all the delays in ascending order.

    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay in seconds for each wait_random call.

    Returns:
        List[float]: The list of all delays in ascending order.
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
