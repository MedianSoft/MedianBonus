from fastapi import Depends

from .repository import get_customer_repository
from ...domain.customer.repository import CustomerRepository
from ...services.customer import CustomerService


def get_customer_service(
    repository: CustomerRepository = Depends(get_customer_repository),
) -> CustomerService:
    return CustomerService(repository)
