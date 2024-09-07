# Configuration settings will be here

# app/core/config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Production Ready FastAPI"
    admin_email: str
    database_url: str

    class Config:
        env_file = ".env"

settings = Settings()
