import uuid

from pydantic import BaseModel, EmailStr

from backend.domain.business import BusinessStatus
from backend.schemas.base import BaseRequest


class BusinessCreateRequest(BaseRequest):
    email: EmailStr
    name: str
    password: str


class BusinessDeleteRequest(BaseRequest):
    id: uuid.UUID


class BusinessGetByEmailRequest(BaseRequest):
    email: EmailStr


class BusinessGetByIDRequest(BaseRequest):
    id: uuid.UUID


class BusinessResponse(BaseModel):
    id: uuid.UUID
    email: EmailStr
    name: str
    status: BusinessStatus


class BusinessListResponse(BaseModel):
    businesses: list[BusinessResponse]
