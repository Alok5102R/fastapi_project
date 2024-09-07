from fastapi import APIRouter

router = APIRouter(prefix='/item_controller', tags=['Items API'])


@router.get('/itemlist', summary="Returns list of items")
def get_normal() -> dict:
    items_list = ["chair","table","fan"]
    response = {
        "status": "Success",
        "data": items_list
    }
    return response