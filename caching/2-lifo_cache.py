#!/usr/bin/python3
""" LIFOCache module
"""

from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """LIFOCache defines a caching system following LIFO algorithm"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """Add an item to the cache"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
            if self.last_key is not None:
                print("DISCARD:", self.last_key)
                del self.cache_data[self.last_key]

        self.cache_data[key] = item
        self.last_key = key

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key, None)
