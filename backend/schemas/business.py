from pydantic import BaseModel, EmailStr

from backend.domain.business import Status


class BusinessCreate(BaseModel):
    email: EmailStr
    password_hash: str

    class Config:
        from_attributes = True


class BusinessDelete(BaseModel):
    email: EmailStr

    class Config:
        from_attributes = True


class BusinessRead(BaseModel):
    id: int
    email: EmailStr
    status: Status

    class Config:
        from_attributes = True
