import enum


class Status(enum.Enum):
    CREATED = "created"  # создан, настраивается
    ACTIVATED = "activated"  # работает
    STOPPED = "stopped"  # временно приостановлен
    SUSPENDED = "suspended"  # остановлен
