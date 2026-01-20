from backend.domain.store import Store, StoreRepository, StoreStatus
from backend.factories.repository import get_store_repository
from backend.schemas.store import (
    StoreCreateRequest,
    StoreDeleteRequest,
    StoreGetByIDRequest,
    StoreGetByNameRequest,
    StoreListRequest,
    StoreListResponse,
    StoreResponse,
    StoreUpdateRequest,
)
from backend.utils.exception_handler import AlreadyExistsError, NotFoundError


class StoreService:
    def __init__(self, repository: StoreRepository = get_store_repository()):
        self.repository = repository

    async def create(self, data: StoreCreateRequest) -> StoreResponse:
        existing = await self.repository.get(name=data.name, business_id=data.business_id)
        if existing:
            raise AlreadyExistsError("Store")

        store = Store(name=data.name, business_id=data.business_id)
        result = await self.repository.create(store)

        return StoreResponse.model_validate(result)

    async def delete(self, data: StoreDeleteRequest) -> StoreResponse | None:
        existing = await self.repository.get_by_id(data.id)
        if not existing:
            raise NotFoundError("Store")

        existing.status = StoreStatus.SUSPENDED
        result = await self.repository.update(existing)

        return StoreResponse.model_validate(result)

    async def update(self, data: StoreUpdateRequest) -> StoreResponse | None:
        existing = await self.repository.get(name=data.name, business_id=data.business_id)
        if not existing:
            raise NotFoundError("Store")

        existing.status = data.status
        existing.name = data.name
        result = await self.repository.update(existing)

        return StoreResponse.model_validate(result)

    async def get(self, data: StoreGetByNameRequest) -> StoreResponse | None:
        result = await self.repository.get(name=data.name, business_id=data.business_id)
        if not result:
            raise NotFoundError("Store")

        return StoreResponse.model_validate(result)

    async def get_by_id(self, data: StoreGetByIDRequest) -> StoreResponse | None:
        result = await self.repository.get_by_id(data.id)
        if not result:
            raise NotFoundError("Store")

        return StoreResponse.model_validate(result)

    async def get_all(self, data: StoreListRequest) -> StoreListResponse:
        result = await self.repository.get_all(business_id=data.business_id)
        if not result:
            raise NotFoundError("Store")

        return StoreListResponse(storees=[StoreResponse.model_validate(store) for store in result])
