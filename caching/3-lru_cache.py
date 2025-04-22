#!/usr/bin/python3
""" LRUCache module
"""

from base_caching import BaseCaching

class LRUCache(BaseCaching):
    """LRUCache defines a caching system with LRU eviction policy"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """Add an item to the cache with LRU eviction"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.usage_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.usage_order.pop(0)
            del self.cache_data[lru_key]
            print("DISCARD:", lru_key)

        self.cache_data[key] = item
        self.usage_order.append(key)

    def get(self, key):
        """Retrieve an item from the cache and update its usage"""
        if key is None or key not in self.cache_data:
            return None

        # Move accessed key to the end to mark it as recently used
        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]
