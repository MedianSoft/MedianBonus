import uuid
from typing import TYPE_CHECKING

from backend.domain.bonus import Bonus
from backend.factories.repository import get_bonus_repository
from backend.schemas.bonus import (
    BonusListResponse,
    BonusResponse,
)
from backend.utils.exception_handler import NotFoundError

if TYPE_CHECKING:
    import uuid

    from backend.domain.bonus import BonusRepository
    from backend.schemas.bonus import (
        BonusCreateRequest,
        BonusDeleteRequest,
        BonusUpdateRequest,
    )


class BonusService:
    def __init__(self, repository: "BonusRepository" = get_bonus_repository()):
        self.repository = repository

    async def create(self, data: "BonusCreateRequest") -> BonusResponse:
        bonus = Bonus(
            type=data.type,
            store_id=data.store_id,
            product_id=data.product_id,
            parameter=data.parameter,
        )
        result = await self.repository.create(bonus)

        return BonusResponse.model_validate(result)

    async def update(self, data: "BonusUpdateRequest") -> BonusResponse:
        existing = await self.repository.get(Bonus, data.id)
        if not existing:
            raise NotFoundError("Store")

        if data.parameter:
            existing.value = data.parameter
        if data.product_id:
            existing.product_id = data.product_id

        result = await self.repository.update(existing)

        return BonusResponse.model_validate(result)

    async def delete(self, data: "BonusDeleteRequest") -> None:
        existing = await self.repository.get(Bonus, data.id)
        if not existing:
            raise NotFoundError("Bonus")

        existing.is_active = False
        _ = await self.repository.update(existing)

    async def get(self, id: "uuid.UUID") -> BonusResponse:  # noqa
        result = await self.repository.get(Bonus, id)
        if not result:
            raise NotFoundError("Bonus")

        return BonusResponse.model_validate(result)

    async def get_all(self) -> "BonusListResponse":
        result = await self.repository.get_all(Bonus)
        if not result:
            raise NotFoundError("Bonuses")

        return BonusListResponse(bonuses=[BonusResponse.model_validate(bonus) for bonus in result])
