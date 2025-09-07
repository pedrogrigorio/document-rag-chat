from datetime import datetime

from beanie import Document
from pydantic import Field


class UserModel(Document):
    email: str
    password_hash: str
    created_at: datetime = Field(default_factory=datetime.now)

    class Settings:
        name = "users"
