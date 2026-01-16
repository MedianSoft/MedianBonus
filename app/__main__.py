from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.database.bootstrap import init_database


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_database()
    yield


if __name__ == "__main__":
    app = FastAPI()
    uvicorn.run(
        "app.__main__:app",
        host="0.0.0.0",
        port=8000,
        reload=False,
    )
