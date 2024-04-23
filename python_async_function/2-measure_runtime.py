import asyncio
import random
import time
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
    Asynchronous routine that spawns wait_random n times with the specified max_delay
    and returns the list of all the delays in ascending order.
    
    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay in seconds for each wait_random call.
        
    Returns:
        List[float]: The list of all delays in ascending order.
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)

def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and returns the average time per operation.
    
    Args:
        n (int): The number of times to call wait_n.
        max_delay (int): The maximum delay in seconds for each wait_random call.
        
    Returns:
        float: The average time per operation.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
