#!/usr/bin/python3
"""FIFOCache module that inherits from BaseCaching"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A FIFO caching system"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.order = []  # List to keep track of insertion order

    def put(self, key, item):
        """Assign the item to the key in the cache (FIFO)"""
        if key is None or item is None:
            return

        if key not in self.cache_data:
            self.order.append(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Remove the first inserted key
            discard_key = self.order.pop(0)
            del self.cache_data[discard_key]
            print("DISCARD:", discard_key)

    def get(self, key):
        """Return the item linked to key, or None if not found"""
        return self.cache_data.get(key, None)
