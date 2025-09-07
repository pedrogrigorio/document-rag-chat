from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from api import register_routes
from core.db.mongo import init_db
from core.logger import configure_logging


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    await init_db()
    yield


# debug, info, warning, error, critical
configure_logging("info")

app = FastAPI(lifespan=lifespan)

register_routes(app)
