import uuid

from app.domain.bonus import BonusType
from app.schema.base import BaseRequest, BaseResponse


class BonusCreateRequest(BaseRequest):
    type: BonusType
    store_id: uuid.UUID
    product_id: uuid.UUID
    value: int


class BonusUpdateRequest(BaseRequest):
    id: uuid.UUID
    product_id: uuid.UUID
    value: int | None


class BonusDeleteRequest(BaseRequest):
    id: uuid.UUID


class BonusGetAllByStore(BaseRequest):
    store_id: uuid.UUID


class BonusResponse(BaseResponse):
    id: uuid.UUID
    type: BonusType
    store_id: uuid.UUID
    producte_id: uuid.UUID | None
    value: int
    is_active: bool


class BonusListResponse(BaseResponse):
    bonuses: list[BonusResponse]
