from typing import TYPE_CHECKING

from app.domain.base import Status
from app.domain.store import Store
from app.schema.store import (
    StoreListResponse,
    StoreResponse,
)
from app.util.exception_handler import AlreadyExistsError, NotFoundError

if TYPE_CHECKING:
    import uuid

    from app.domain.store import StoreRepository
    from app.schema.store import (
        StoreAllByBusinessRequest,
        StoreCreateRequest,
        StoreDeleteRequest,
        StoreGetByNameInBusinessRequest,
        StoreUpdateRequest,
    )


class StoreService:
    def __init__(self, repository: "StoreRepository"):
        self.repository = repository

    async def create(self, data: "StoreCreateRequest") -> StoreResponse:
        existing = await self.repository.get_by_name_in_business(name=data.name, business_id=data.business_id)
        if existing:
            raise AlreadyExistsError("Store")

        store = Store(name=data.name, business_id=data.business_id)
        result = await self.repository.create(store)
        return StoreResponse.model_validate(result)

    async def update(self, data: "StoreUpdateRequest") -> StoreResponse:
        existing = await self.repository.get(Store, data.id)
        if not existing:
            raise NotFoundError("Store")

        if data.name:
            existing.name = data.name

        result = await self.repository.update(existing)
        return StoreResponse.model_validate(result)

    async def delete(self, data: "StoreDeleteRequest") -> None:
        existing = await self.repository.get(Store, data.id)
        if not existing:
            raise NotFoundError("Store")

        existing.status = Status.SUSPENDED
        _ = await self.repository.update(existing)

    async def get(self, id: "uuid.UUID") -> StoreResponse:  # noqa
        result = await self.repository.get(Store, id)
        if not result:
            raise NotFoundError("Store")

        return StoreResponse.model_validate(result)

    async def get_all(self) -> StoreListResponse:
        result = await self.repository.get_all(Store)
        if not result:
            raise NotFoundError("Store")

        return StoreListResponse(storees=[StoreResponse.model_validate(store) for store in result])

    async def get_by_name_in_business(self, data: "StoreGetByNameInBusinessRequest") -> StoreResponse:
        result = await self.repository.get_by_name_in_business(name=data.name, business_id=data.business_id)
        if not result:
            raise NotFoundError("Store")

        return StoreResponse.model_validate(result)

    async def get_all_by_business(self, data: "StoreAllByBusinessRequest") -> StoreListResponse:
        result = await self.repository.get_all_by_business(business_id=data.business_id)
        if not result:
            raise NotFoundError("Store")

        return StoreListResponse(storees=[StoreResponse.model_validate(store) for store in result])
