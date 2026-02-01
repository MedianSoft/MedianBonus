import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import (
    auth_router,
    bonus_router,
    business_router,
    customer_router,
    employee_router,
    order_router,
    product_router,
    store_router,
)
from app.setting.app import app_settings
from app.util.exception_handler import register_exception_handlers

app = FastAPI(title="MedianBonus")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_exception_handlers(app)

routers = [
    auth_router,
    bonus_router,
    business_router,
    customer_router,
    employee_router,
    order_router,
    product_router,
    store_router,
]
for router in routers:
    app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(
        "app.__main__:app",
        host=app_settings.host,
        port=app_settings.port,
        reload=False,
    )
