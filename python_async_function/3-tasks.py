#!/usr/bin/env python3
import asyncio
import random

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

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes an integer max_delay and returns an asyncio.Task for wait_random(max_delay).
    
    Args:
        max_delay (int): The maximum delay in seconds.
        
    Returns:
        asyncio.Task: An asyncio.Task object for the wait_random coroutine with the specified max_delay.
    """
    return asyncio.create_task(wait_random(max_delay))
