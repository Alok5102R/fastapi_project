# Business logic for user will be here
# app/services/user_service.py
from sqlalchemy.orm import Session
from app.models.user import User

def create_user(db: Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()
