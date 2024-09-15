from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.user import User, UserSchema
from app.services.db_service import create_row, get_row
from pydantic import BaseModel

class SuccessResponse(BaseModel):
    message: str = "Operation Successful"
    data:  dict


router = APIRouter(prefix='/users')

@router.post("/", response_model=SuccessResponse)
async def create_user_endpoint(user: UserSchema, db: Session = Depends(get_db)):
    user_details = User(
        username = user.username,
        email = user.email,
        hashed_password = user.hashed_password
    )
    new_user = create_row(db,  user_details)

    # new_user = create_user(db, user_details)
    response = SuccessResponse(
        message="User created successfully",
        data= {
            "id": new_user.id,
            "username": new_user.username,
            "email": new_user.email
        }
    )
    return response

@router.get("/{user_id}", response_model=SuccessResponse)
async def get_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    # user = get_user(db, user_id)
    user = get_row(db, User, user_id)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    response = SuccessResponse(
        message="User fetched successfully",
        data= {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
    )
    return response