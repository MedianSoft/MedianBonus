import uuid

from pydantic import BaseModel

from backend.domain.bonus import BonusType
from backend.schemas.base import BaseRequest


class BonusCreateRequest(BaseRequest):
    type: BonusType
    store_id: uuid.UUID
    product_id: uuid.UUID | None
    parameter: int


class BonusDeleteRequest(BaseRequest):
    id: uuid.UUID


class BonusGetByIDRequest(BaseRequest):
    id: uuid.UUID


class BonusResponse(BaseModel):
    id: uuid.UUID
    type: BonusType
    store_id: uuid.UUID
    producte_id: uuid.UUID | None
    parameter: int
    is_active: bool


class BonusListResponse(BaseModel):
    bonuses: list[BonusResponse]
