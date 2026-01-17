from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from backend.api import business_router, customer_router, store_router
from backend.database.bootstrap import drop_database, init_database
from backend.settings import app_settings


@asynccontextmanager
async def lifespan(app: FastAPI):  # noqa
    await init_database()
    yield
    if app_settings.env == "dev":
        await drop_database()  # for early dev purposes only


app = FastAPI(lifespan=lifespan)
routers = [business_router, customer_router, store_router]
for router in routers:
    app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(
        "backend.__main__:app",
        host=app_settings.host,
        port=app_settings.port,
        reload=False,
    )
