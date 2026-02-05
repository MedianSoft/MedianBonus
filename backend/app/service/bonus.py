import uuid
from typing import TYPE_CHECKING

from app.domain.bonus import Bonus
from app.schema.bonus import BonusGetAllByStore, BonusListResponse, BonusResponse
from app.util.exception_handler import NotFoundError

if TYPE_CHECKING:
    import uuid

    from app.domain.bonus import BonusRepository
    from app.schema.bonus import (
        BonusCreateRequest,
        BonusDeleteRequest,
        BonusUpdateRequest,
    )


class BonusService:
    def __init__(self, repository: "BonusRepository"):
        self.repository = repository

    async def create(self, data: "BonusCreateRequest") -> BonusResponse:
        bonus = Bonus(
            type=data.type,
            store_id=data.store_id,
            product_id=data.product_id,
            value=data.value,
        )
        result = await self.repository.create(bonus)
        return BonusResponse.model_validate(result)

    async def update(self, data: "BonusUpdateRequest") -> BonusResponse:
        existing = await self.repository.get(model=Bonus, id=data.id)
        if not existing:
            raise NotFoundError("Store")

        if data.value:
            existing.value = data.value
        if data.product_id:
            existing.product_id = data.product_id
        result = await self.repository.update(existing)
        return BonusResponse.model_validate(result)

    async def delete(self, data: "BonusDeleteRequest") -> None:
        existing = await self.repository.get(model=Bonus, id=data.id)
        if not existing:
            raise NotFoundError("Bonus")

        existing.is_active = False
        _ = await self.repository.update(existing)

    async def get(self, id: "uuid.UUID") -> BonusResponse:  # noqa
        result = await self.repository.get(model=Bonus, id=id)
        if not result:
            raise NotFoundError("Bonus")

        return BonusResponse.model_validate(result)

    async def get_all(self) -> "BonusListResponse":
        result = await self.repository.get_all(model=Bonus)
        if not result:
            raise NotFoundError("Bonuses")

        return BonusListResponse(bonuses=[BonusResponse.model_validate(bonus) for bonus in result])

    async def get_all_by_store(self, data: "BonusGetAllByStore") -> "BonusListResponse":
        result = await self.repository.get_all_by_store(data.store_id)
        if not result:
            raise NotFoundError("Bonuses")

        return BonusListResponse(bonuses=[BonusResponse.model_validate(bonus) for bonus in result])
