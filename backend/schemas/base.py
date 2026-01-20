from pydantic import BaseModel


class BaseRequest(BaseModel):
    class Config:
        from_attributes = True
