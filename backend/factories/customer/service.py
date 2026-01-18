from fastapi import Depends

from ...domain.customer.repository import CustomerRepository
from ...services.customer import CustomerService
from .repository import get_customer_repository


def get_customer_service(
    repository: CustomerRepository = Depends(get_customer_repository),
) -> CustomerService:
    return CustomerService(repository)
