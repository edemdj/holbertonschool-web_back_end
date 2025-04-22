#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - cache_data: dictionary
      - MAX_ITEMS: maximum number of items before discarding
    """
    MAX_ITEMS = 4

    def __init__(self):
        """Initialize the cache_data dictionary"""
        self.cache_data = {}

    def print_cache(self):
        """Print the contents of the cache"""
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print(f"{key}: {self.cache_data[key]}")
