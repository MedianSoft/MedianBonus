from fastapi import Depends

from ...domain.product.repository import ProductRepository
from ...services.product import ProductService
from .repository import get_product_repository


def get_product_service(
    repository: ProductRepository = Depends(get_product_repository),
) -> ProductService:
    return ProductService(repository)
