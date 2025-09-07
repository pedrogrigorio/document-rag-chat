import logging
import os
from typing import Any

from beanie import init_beanie  # type: ignore
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from core.utils import mask_url
from modules.documents.model import DocumentModel
from modules.users.model import UserModel

load_dotenv()

CLIENT_URL = os.getenv("DB_CLIENT_URL")
DB_NAME = os.getenv("DB_NAME")

if CLIENT_URL is None:
    msg = "CLIENT_URL environment variable not set"
    logging.error(msg)
    raise RuntimeError(msg)

client: AsyncIOMotorClient[Any] | None = None

if DB_NAME is None:
    msg = "DB_NAME environment variable not set"
    logging.error(msg)
    raise RuntimeError(msg)


async def init_db() -> None:
    global client
    logging.info("Inicializando conexão com o banco de dados...")

    client = AsyncIOMotorClient(CLIENT_URL)

    masked_url = mask_url(CLIENT_URL)
    logging.debug(f"Conectando ao MongoDB em {masked_url}, DB: {DB_NAME}")

    try:
        await init_beanie(
            database=client[DB_NAME],  # type: ignore[arg-type]
            document_models=[UserModel, DocumentModel],
        )
        logging.info(f"Banco de dados '{DB_NAME}' inicializado com sucesso.")
    except Exception:
        logging.exception("Falha ao inicializar o banco de dados")
        raise


def get_db() -> AsyncIOMotorDatabase[Any]:
    if client is None:
        msg = "Database not initialized"
        raise RuntimeError(msg)

    return client[DB_NAME]  # type: ignore
