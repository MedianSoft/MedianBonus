from fastapi import Depends

from ...domain.store.repository import StoreRepository
from ...services.store import StoreService
from .repository import get_store_repository


def get_store_service(
    repository: StoreRepository = Depends(get_store_repository),
) -> StoreService:
    return StoreService(repository)
