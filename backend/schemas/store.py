from pydantic import BaseModel

from backend.domain.store import Status


class StoreCreate(BaseModel):
    name: str


class StoreRead(BaseModel):
    id: int
    name: str
    status: Status

    class Config:
        from_attributes = True
