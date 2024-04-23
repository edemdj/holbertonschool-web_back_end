#!/usr/bin/env python3
from typing import List
import random
import asyncio


async_generator = __import__("0-async_generator").async_generator

async def async_comprehension() -> List[float]:
    """
    Coroutine qui utilise une compréhension asynchrone pour collecter 10 nombres aléatoires
    en utilisant async_generator, puis retourne les 10 nombres aléatoires.
    
    Returns:
        List[float]: La liste des 10 nombres aléatoires.
    """

    random_numbers = [number async for number in async_generator()]
    return random_numbers


async def main():
    numbers = await async_comprehension()
    print(numbers)


asyncio.run(main())
