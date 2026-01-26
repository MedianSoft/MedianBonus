from pydantic import BaseModel, ConfigDict


class BaseRequest(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class BaseResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
