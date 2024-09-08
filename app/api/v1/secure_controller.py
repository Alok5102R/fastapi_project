# app/api/v1/secure_route.py
from fastapi import APIRouter, Depends
from app.core.dependencies import validate_api_key

router = APIRouter(
    prefix="/secure",
    tags=["secure"],
    dependencies=[Depends(validate_api_key)]
)

@router.get("/")
async def secure_endpoint():
    return {"message": "Secure Endpoint Accessed"}