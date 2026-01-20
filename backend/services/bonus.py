from backend.domain.bonus import Bonus, BonusRepository
from backend.factories.repository import get_bonus_repository
from backend.schemas.bonus import (
    BonusCreateRequest,
    BonusDeleteRequest,
    BonusGetByIDRequest,
    BonusListResponse,
    BonusResponse,
)
from backend.utils.exception_handler import NotFoundError


class BonusService:
    def __init__(self, repository: BonusRepository = get_bonus_repository()):
        self.repository = repository

    async def create(self, data: BonusCreateRequest) -> BonusResponse:
        bonus = Bonus(
            type=data.type,
            store_id=data.store_id,
            product_id=data.product_id,
            parameter=data.parameter,
        )
        result = await self.repository.create(bonus)

        return BonusResponse.model_validate(result)

    async def delete(self, data: BonusDeleteRequest) -> BonusResponse | None:
        existing = await self.repository.get(data.id)
        if not existing:
            raise NotFoundError("Bonus")

        existing.is_active = False
        result = await self.repository.update(existing)

        return BonusResponse.model_validate(result)

    async def get(self, data: BonusGetByIDRequest) -> BonusResponse | None:
        result = await self.repository.get(data.id)
        if not result:
            raise NotFoundError("Bonus")

        return BonusResponse.model_validate(result)

    async def get_all(self) -> BonusListResponse:
        result = await self.repository.get_all()
        if not result:
            raise NotFoundError("Bonuses")

        return BonusListResponse(bonuses=[BonusResponse.model_validate(bonus) for bonus in result])
