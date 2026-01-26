from .auth import router as auth_router
from .bonus import router as bonus_router
from .business import router as business_router
from .customer import router as customer_router
from .employee import router as employee_router
from .order import router as order_router
from .product import router as product_router
from .store import router as store_router

__all__ = [
    "bonus_router",
    "business_router",
    "customer_router",
    "employee_router",
    "order_router",
    "product_router",
    "store_router",
    "auth_router",
]
