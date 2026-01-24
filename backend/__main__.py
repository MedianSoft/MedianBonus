from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import Any

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api import (
    bonus_router,
    business_router,
    customer_router,
    employee_router,
    order_router,
    product_router,
    store_router,
    auth_router,
)
from backend.database.bootstrap import drop_database, init_database
from backend.setting import app_settings
from backend.util.exception_handler import register_exception_handlers


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, Any]:  # noqa
    await init_database()
    yield
    if app_settings.env == "dev":
        await drop_database()  # for early dev purposes only


app = FastAPI(lifespan=lifespan, title="MedianBonus")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_exception_handlers(app)

routers = [
    bonus_router,
    business_router,
    customer_router,
    employee_router,
    order_router,
    product_router,
    store_router,
    auth_router,
]
for router in routers:
    app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(
        "backend.__main__:app",
        host=app_settings.host,
        port=app_settings.port,
        reload=False,
    )
