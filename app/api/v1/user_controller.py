# Routers relates to user will be here
# app/api/v1/users.py
from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session
# from app.db.session import get_db
# from app.models.user import User
# from app.services.user_service import create_user, get_user

router = APIRouter(prefix='/user_controller')

# @router.post("/users", response_model=User)
# async def create_user_endpoint(user: User, db: Session = Depends(get_db)):
#     return create_user(db, user)

# @router.get("/users/{user_id}", response_model=User)
# async def get_user_endpoint(user_id: int, db: Session = Depends(get_db)):
#     user = get_user(db, user_id)
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
#     return user
