from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr

from app.models.user_model import UserRole


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr


class UserCreate(UserBase):
    password: str
    role: Optional[UserRole] = UserRole.user


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(UserBase):
    id: int
    role: UserRole

    model_config = ConfigDict(from_attributes=True)


class UserAuthInfo(BaseModel):
    id: int
    role: UserRole

    model_config = ConfigDict(from_attributes=True)
