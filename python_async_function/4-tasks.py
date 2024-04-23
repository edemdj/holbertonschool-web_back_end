#!/usr/bin/env python3
import asyncio
from typing import List
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay seconds and returns it.
    
    Args:
        max_delay (int, optional): The maximum delay in seconds (default is 10).
        
    Returns:
        float: The random delay.
    """
    await asyncio.sleep(random.uniform(0, max_delay))
    return max_delay

async def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes an integer max_delay and returns an asyncio.Task for wait_random(max_delay).
    
    Args:
        max_delay (int): The maximum delay in seconds.
        
    Returns:
        asyncio.Task: An asyncio.Task object for the wait_random coroutine with the specified max_delay.
    """
    return asyncio.create_task(wait_random(max_delay))

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns task_wait_random n times with the specified max_delay
    and returns the list of all the delays in ascending order.
    
    Args:
        n (int): The number of times to call task_wait_random.
        max_delay (int): The maximum delay in seconds for each wait_random call.
        
    Returns:
        List[float]: The list of all delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    delays = [await result for result in results]
    return sorted(delays)