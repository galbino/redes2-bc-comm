from pydantic import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    BASE_URL: Optional[str]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
