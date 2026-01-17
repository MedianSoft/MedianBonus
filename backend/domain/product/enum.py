import enum


class Status(enum.Enum):
    AVAILABLE = "available"
    NOT_AVAILABLE = "not_available"
    REMOVED = "removed"


class Category(enum.Enum):
    FOOD = "food"
    DRINK = "drink"
    OTHER = "other"
