import uuid

from app.domain.store import StoreStatus
from app.schema.base import BaseRequest, BaseResponse


class StoreCreateRequest(BaseRequest):
    name: str
    business_id: uuid.UUID


class StoreDeleteRequest(BaseRequest):
    id: uuid.UUID


class StoreUpdateRequest(BaseRequest):
    id: uuid.UUID
    name: str


class StoreGetByNameInBusinessRequest(BaseRequest):
    name: str
    business_id: uuid.UUID


class StoreAllByBusinessRequest(BaseRequest):
    business_id: uuid.UUID


class StoreResponse(BaseResponse):
    id: uuid.UUID
    business_id: uuid.UUID
    name: str
    status: StoreStatus


class StoreListResponse(BaseResponse):
    storees: list[StoreResponse]
