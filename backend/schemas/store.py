import uuid

from pydantic import BaseModel

from backend.domain.store import StoreStatus
from backend.schemas.base import BaseRequest


class StoreCreateRequest(BaseRequest):
    name: str
    business_id: uuid.UUID


class StoreDeleteRequest(BaseRequest):
    id: uuid.UUID


class StoreUpdateRequest(BaseRequest):
    name: str
    new_name: str
    business_id: uuid.UUID
    status: StoreStatus


class StoreGetByNameRequest(BaseRequest):
    name: str
    business_id: uuid.UUID


class StoreGetByIDRequest(BaseRequest):
    id: uuid.UUID


class StoreListRequest(BaseRequest):
    business_id: uuid.UUID


class StoreResponse(BaseModel):
    id: uuid.UUID
    business_id: uuid.UUID
    name: str
    status: StoreStatus


class StoreListResponse(BaseModel):
    storees: list[StoreResponse]
