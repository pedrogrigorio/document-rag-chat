from datetime import datetime

from beanie import Document
from pydantic import Field


class DocumentModel(Document):
    user_id: str
    filename: str
    tags: list[str]
    created_at: datetime = Field(default_factory=datetime.now)

    class Settings:
        name = "documents"
