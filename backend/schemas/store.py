import uuid

from pydantic import BaseModel

from backend.domain.store import StoreStatus


class StoreCreateRequest(BaseModel):
    name: str
    business_id: uuid.UUID


class StoreDeleteRequest(BaseModel):
    name: str
    business_id: uuid.UUID


class StoreUpdateRequest(BaseModel):
    name: str
    new_name: str
    business_id: uuid.UUID
    status: StoreStatus


class StoreGetByNameRequest(BaseModel):
    name: str
    business_id: uuid.UUID


class StoreListRequest(BaseModel):
    business_id: uuid.UUID


class StoreResponse(BaseModel):
    id: uuid.UUID
    business_id: uuid.UUID
    name: str
    status: StoreStatus

    class Config:
        from_attributes = True


class StoreListResponse(BaseModel):
    storees: list[StoreResponse]
