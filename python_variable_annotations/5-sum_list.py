#!/usr/bin/env python3
"""function sum_list which takes a list input_list of floats as argument"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Takes a list of floats as input and returns their sum as a float.

    Args:
        input_list (List[float]): The list of floats.

    Returns:
        float: The sum of the floats in the input_list.
    """
    return sum(input_list)
