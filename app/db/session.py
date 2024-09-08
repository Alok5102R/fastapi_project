# Database session and connection management

# app/db/session.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

SQLALCHEMY_DATABASE_URL = settings.database_url

engine = create_engine(  
    SQLALCHEMY_DATABASE_URL,
    pool_size=10,          # The size of the connection pool
    max_overflow=20,       # The maximum number of connections to allow above pool_size
    pool_timeout=30,       # The maximum number of seconds to wait for a connection
    pool_recycle=1800      # Recycle connections after 1800 seconds
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
