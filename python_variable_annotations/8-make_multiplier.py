#!/usr/bin/env python3
"""function make_multiplier that takes a float multiplier"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float multiplier as input and returns a function that multiplies a float by multiplier.
    
    Args:
        multiplier (float): The multiplier value.
        
    Returns:
        Callable[[float], float]: A function that multiplies a float by the multiplier.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
