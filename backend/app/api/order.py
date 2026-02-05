from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status

from app.container.base import BaseContainer
from app.schema.order import OrderRequest, OrderResponse
from app.service.order import OrderService

router = APIRouter(prefix="/order", tags=["order"])


@router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
    response_model=OrderResponse,
)
@inject
async def create(
    data: OrderRequest,
    service: OrderService = Depends(Provide[BaseContainer.order.service]),  # type: ignore
) -> OrderResponse:
    return await service.create(data)
