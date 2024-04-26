#!/usr/bin/env python3
"""Module with foction that coverts int or float to tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string and an int or float as input and returns a tuple.
    The first element of the tuple is the string k.
    The second element is the square of the int/float v.

    Args:
        k (str): The string key.
        v (Union[int, float]): The int or float value.

    Returns:
        Tuple[str, float]: A tuple containing k and the square of v.
    """
    return (k, v * v)
