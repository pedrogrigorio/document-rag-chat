from fastapi import FastAPI

from modules.documents.controller import router as documents_router
from modules.tags.controller import router as tags_router
from modules.users.controller import router as users_router


def register_routes(app: FastAPI) -> None:
    app.include_router(documents_router)
    app.include_router(users_router)
    app.include_router(tags_router)
