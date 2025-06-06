#!/usr/bin/env python3
def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of size two containing a start index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
