from typing import TYPE_CHECKING

from app.domain.base import Status
from app.domain.customer import Customer
from app.schema.customer import (
    CustomerListResponse,
    CustomerResponse,
)
from app.util.exception_handler import NotFoundError

if TYPE_CHECKING:
    import uuid

    from app.domain.customer import CustomerRepository
    from app.schema.customer import (
        CustomerCreateRequest,
        CustomerDeleteRequest,
        CustomerGetByPhoneRequest,
        CustomerUpdateRequest,
    )


class CustomerService:
    def __init__(self, repository: "CustomerRepository") -> None:
        self.repository = repository

    async def create(self, data: "CustomerCreateRequest") -> CustomerResponse:
        existing = await self.repository.get_by_phone(data.phone)
        if existing:
            return CustomerResponse.model_validate(existing)

        customer = Customer(name=data.name, phone=data.phone)
        result = await self.repository.create(customer)
        return CustomerResponse.model_validate(result)

    async def update(self, data: "CustomerUpdateRequest") -> CustomerResponse:
        existing = await self.repository.get(Customer, data.id)
        if not existing:
            raise NotFoundError("Customer")

        if data.phone:
            existing.phone = data.phone
        if data.name:
            existing.name = data.name

        result = await self.repository.update(existing)

        return CustomerResponse.model_validate(result)

    async def delete(self, data: "CustomerDeleteRequest") -> None:
        existing = await self.repository.get(Customer, data.id)
        if not existing:
            raise NotFoundError("Customer")

        existing.status = Status.SUSPENDED
        _ = await self.repository.update(existing)

    async def get(self, id: "uuid.UUID") -> CustomerResponse:  # noqa
        result = await self.repository.get(Customer, id)
        if not result:
            raise NotFoundError("Customer")

        return CustomerResponse.model_validate(result)

    async def get_all(self) -> CustomerListResponse:
        result = await self.repository.get_all(Customer)
        if not result:
            raise NotFoundError("Customers")

        return CustomerListResponse(customers=[CustomerResponse.model_validate(customer) for customer in result])

    async def get_by_phone(self, data: "CustomerGetByPhoneRequest") -> CustomerResponse:
        result = await self.repository.get_by_phone(data.phone)
        if not result:
            raise NotFoundError("Customer")

        return CustomerResponse.model_validate(result)
