# app/api/v1/cache_controller.py
from fastapi import APIRouter, Depends
from app.core.cache import CacheDependency, get_cache

router = APIRouter(
    prefix="/cache_router",
    tags=["Cache API"],
)

@router.get("/{key}")
async def get_cache_item(key: str, cache: CacheDependency = Depends(get_cache)):
    item = cache.get_from_cache(key)
    if item is None:
        return {"detail": "Item not found"}
    return {"item": item}

@router.post("/{key}")
async def set_cache_item(key: str, value: str, cache: CacheDependency = Depends(get_cache)):
    cache.set_to_cache(key, value)
    return {"detail": "Item set successfully"}
