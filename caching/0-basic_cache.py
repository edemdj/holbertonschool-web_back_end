#!/usr/bin/python3
""" BasicCache module """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache - no limit caching system """

    def put(self, key, item):
        """ Assign item to key in the cache_data dictionary """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Return the value linked to key in cache_data, or None """
        return self.cache_data.get(key, None)
