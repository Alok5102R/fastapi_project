# app/core/cache.py
from fastapi import Depends
from cachetools import TTLCache
import logging

logging.basicConfig(level=logging.INFO)

class CacheDependency:
    def __init__(self):
        self.cache = TTLCache(maxsize=100, ttl=300)  #max data = 100, time to live = 300s (5 minutes)

    def get_from_cache(self, key: str) -> str:
        return self.cache.get(key)

    def set_to_cache(self, key: str, value: str):
        logging.info(f"Setting key: {key}")
        self.cache[key] = value
        logging.info(f"Key set: {key}")

def get_cache() -> CacheDependency:
    return CacheDependency()
