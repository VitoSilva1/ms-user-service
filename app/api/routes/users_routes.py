from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas import user_schema
from app.services import user_service

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/user", response_model=user_schema.UserResponse)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)


@router.get("/", response_model=list[user_schema.UserResponse])
def list_users(db: Session = Depends(get_db)):
    return user_service.get_all_users(db)


@router.get("/{user_id}", response_model=user_schema.UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return user_service.get_user_by_id(db, user_id)
