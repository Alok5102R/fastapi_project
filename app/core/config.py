from pydantic import BaseModel
from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    # Application settings
    app_name: str = "Production Ready FastAPI"
    environment: str
    debug: bool = False

    # Database settings
    database_url: str

    # Security settings
    secret_key: str
    ALLOWED_HOSTS: str = "*"

    # CORS settings
    cors_origins: str = "*"

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()