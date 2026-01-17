from backend.domain.store import Status, Store, StoreRepository
from backend.factories.store import get_store_repository
from backend.schemas.store import (
    StoreCreateRequest,
    StoreDeleteRequest,
    StoreGetByNameRequest,
    StoreListRequest,
    StoreListResponse,
    StoreResponse,
    StoreUpdateRequest,
)


class StoreService:
    def __init__(self, repository: StoreRepository = get_store_repository()):
        self.repository = repository

    async def create(self, data: StoreCreateRequest) -> StoreResponse:
        existing = await self.repository.get_by_name(
            name=data.name, business_id=data.business_id
        )
        if existing:
            raise ValueError("Store already exists")
        store = Store(name=data.name, business_id=data.business_id)
        result = await self.repository.create(store)
        return StoreResponse.model_validate(result)

    async def delete(self, data: StoreDeleteRequest) -> StoreResponse | None:
        existing = await self.repository.get_by_name(
            name=data.name, business_id=data.business_id
        )
        if not existing:
            raise ValueError("Store doesn't exist")
        existing.status = Status.SUSPENDED
        result = await self.repository.update(existing)
        return StoreResponse.model_validate(result)

    async def update(self, data: StoreUpdateRequest) -> StoreResponse | None:
        existing = await self.repository.get_by_name(
            name=data.name, business_id=data.business_id
        )
        if not existing:
            raise ValueError("Store doesn't exist")
        existing.status = data.status
        existing.name = data.name
        result = await self.repository.update(existing)
        return StoreResponse.model_validate(result)

    async def get_by_name(self, data: StoreGetByNameRequest) -> StoreResponse | None:
        result = await self.repository.get_by_name(
            name=data.name, business_id=data.business_id
        )
        return StoreResponse.model_validate(result)

    async def get_all(self, data: StoreListRequest) -> StoreListResponse:
        result = await self.repository.get_all(business_id=data.business_id)
        return StoreListResponse(
            storees=[StoreResponse.model_validate(store) for store in result]
        )
