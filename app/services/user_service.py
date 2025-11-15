from typing import Optional, Sequence

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.models.user_model import User, UserRole
from app.schemas.user_schema import UserCreate


DEFAULT_ADMINS: Sequence[dict[str, str]] = (
    {
        "first_name": "Admin",
        "last_name": "Jose",
        "email": "admin_jose@fintruck.com",
        "password": "admin_jose",
    },
    {
        "first_name": "Admin",
        "last_name": "Victor",
        "email": "admin_victor@fintruck.com",
        "password": "admin_victor",
    },
)


def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    new_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password=hashed_password,
        role=UserRole.user
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all_users(db: Session):
    return db.query(User).all()


def get_user_by_id(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def get_user_by_email(db: Session, email: str) -> Optional[User]:
    return db.query(User).filter(User.email == email).first()


def authenticate_user(db: Session, email: str, password: str) -> Optional[User]:
    user = get_user_by_email(db, email)
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user


def ensure_default_admins(db: Session) -> None:
    """Create default admin users if they do not exist."""
    created = False
    for admin in DEFAULT_ADMINS:
        if get_user_by_email(db, admin["email"]):
            continue
        hashed_password = get_password_hash(admin["password"])
        new_admin = User(
            first_name=admin["first_name"],
            last_name=admin["last_name"],
            email=admin["email"],
            password=hashed_password,
            role=UserRole.admin,
        )
        db.add(new_admin)
        created = True
    if created:
        db.commit()
