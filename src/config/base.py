from typing import List

from pydantic import BaseSettings as PydanticBaseSettings, PostgresDsn


class BaseSettings(PydanticBaseSettings):
    app_name: str = "FastAPI Boilerplate"
    app_version: str = "0.1.0"
    jwt_secret: str
    reset_password_secret: str
    db_url: PostgresDsn

    model_directories: List[str] = [
        "src.accounts.models",
        "aerich.models"
    ]
