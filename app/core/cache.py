# app/core/cache.py
from fastapi import Depends
from cachetools import TTLCache

class CacheDependency:
    def __init__(self):
        self.cache = TTLCache(maxsize=100, ttl=300)

    def get_from_cache(self, key: str):
        return self.cache.get(key)

    def set_to_cache(self, key: str, value):
        self.cache[key] = value

def get_cache() -> CacheDependency:
    return CacheDependency()
