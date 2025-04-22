#!/usr/bin/python3
""" MRUCache module
"""

from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """MRUCache defines a caching system with MRU eviction policy"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """Add an item to the cache with MRU eviction"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.usage_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.usage_order.pop()
            del self.cache_data[mru_key]
            print("DISCARD:", mru_key)

        self.cache_data[key] = item
        self.usage_order.append(key)

    def get(self, key):
        """Retrieve an item from the cache and update its usage"""
        if key is None or key not in self.cache_data:
            return None

        # Move key to the end to mark it as most recently used
        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]
