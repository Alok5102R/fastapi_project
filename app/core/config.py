# Configuration settings will be here using pydantic like env keys and other required settings
# app/core/config.py
from pydantic import BaseSettings, Field
from typing import List

class Settings(BaseSettings):
    # Application settings
    app_name: str = "Production Ready FastAPI"
    environment: str = Field(..., env="ENVIRONMENT")  # 'development', 'staging', 'production'
    debug: bool = False

    # Database settings
    database_url: str = Field(..., env="DATABASE_URL")  # e.g., mysql://user:password@localhost:3306/mydatabase

    # Security settings
    secret_key: str = Field(..., env="SECRET_KEY")
    allowed_hosts: List[str] = Field(default=["*"], env="ALLOWED_HOSTS")  # Example: ['localhost', 'example.com']

    # CORS settings
    cors_origins: List[str] = Field(default=["*"], env="CORS_ORIGINS")

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()
