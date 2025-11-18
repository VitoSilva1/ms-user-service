<<<<<<< HEAD

from pydantic import BaseModel, EmailStr, Field

class Usuario(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6)
=======
from enum import Enum

from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Enum as SqlEnum

from app.core.database import Base


class UserRole(str, Enum):
    admin = "admin"
    user = "user"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(SqlEnum(UserRole, name="user_role"), default=UserRole.user, nullable=False)
>>>>>>> dec617ad7f81c67c726ae58f65e4f8dcef2e7ed7
