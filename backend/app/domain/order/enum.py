import enum


class OrderStatus(enum.Enum):
    PAID = "paid"
    CANCELLED = "cancelled"
    REFUNDED = "refunded"
