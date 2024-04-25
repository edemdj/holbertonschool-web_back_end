#!/usr/bin/env python3
"""function sum_mixed_list which takes a list mxd_lst"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes a list of integers and floats as input and
    returns their sum as a float.

    Args:
        mxd_lst (List[Union[int, float]]): The list of integers and floats.

    Returns:
        float: The sum of the integers and floats in the mxd_lst.
    """
    return sum(mxd_lst)
