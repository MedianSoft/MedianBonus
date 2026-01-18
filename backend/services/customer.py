from backend.domain.customer.entity import Customer
from backend.domain.customer.repository import CustomerRepository
from backend.factories.customer import get_customer_repository
from backend.schemas.customer import (
    CustomerCreateRequest,
    CustomerGetByPhoneRequest,
    CustomerListResponse,
    CustomerResponse,
)
from backend.utils.exception_handler import NotFoundError


class CustomerService:
    def __init__(self, repository: CustomerRepository = get_customer_repository()) -> None:
        self.repository = repository

    async def create(self, data: CustomerCreateRequest) -> CustomerResponse:
        existing = await self.repository.get_by_phone(data.phone)
        if existing:
            return CustomerResponse.model_validate(existing)

        customer = Customer(name=data.name, phone=data.phone)
        result = await self.repository.create(customer)
        return CustomerResponse.model_validate(result)

    async def get_by_phone(self, data: CustomerGetByPhoneRequest) -> CustomerResponse:
        result = await self.repository.get_by_phone(data.phone)
        if not result:
            raise NotFoundError("Customer")

        return CustomerResponse.model_validate(result)

    async def get_all(self) -> CustomerListResponse:
        result = await self.repository.get_all()
        if not result:
            raise NotFoundError("Customers")

        return CustomerListResponse(customers=[CustomerResponse.model_validate(customer) for customer in result])
