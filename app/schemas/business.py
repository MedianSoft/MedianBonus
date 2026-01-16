from pydantic import BaseModel, EmailStr


class BusinessCreate(BaseModel):
    email: EmailStr
    password_hash: str


class BusinessRead(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    class Config:
        from_attributes = True
