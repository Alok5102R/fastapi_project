# Business logic for user will be here
# app/services/user_service.py
from sqlalchemy.orm import Session


def create_row(db: Session, model_name: type):
    db.add(model_name)
    db.commit()
    db.refresh(model_name)
    return model_name

def get_row(db: Session, model_name: type, row_id: int):
    return db.query(model_name).filter(model_name.id == row_id).first()

def get_all_rows(db: Session, model_name: type):
    return db.query(model_name).all()
