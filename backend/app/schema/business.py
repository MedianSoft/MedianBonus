import uuid

from pydantic import EmailStr

from app.domain.business import BusinessStatus
from app.schema.base import BaseRequest, BaseResponse


class BusinessCreateRequest(BaseRequest):
    email: EmailStr
    name: str
    password: str


class BusinessUpdateRequest(BaseRequest):
    id: uuid.UUID
    email: EmailStr | None
    name: str | None
    password: str | None


class BusinessDeleteRequest(BaseRequest):
    id: uuid.UUID


class BusinessGetByEmailRequest(BaseRequest):
    email: EmailStr


class BusinessResponse(BaseResponse):
    id: uuid.UUID
    email: EmailStr
    name: str
    status: BusinessStatus


class BusinessListResponse(BaseResponse):
    businesses: list[BusinessResponse]
