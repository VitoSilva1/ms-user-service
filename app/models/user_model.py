
from pydantic import BaseModel, EmailStr, Field

class Usuario(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6)
