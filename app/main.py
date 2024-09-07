# app/main.py
from fastapi import FastAPI
from app.api.v1 import user_controller, item_controller  # Importing routers

def create_app() -> FastAPI:
    app = FastAPI(
        title="Production Ready FastAPI",
        description="A FastAPI application with production-ready setup.",
        version="1.0.0",
        docs_url="/api/v1/docs",
        redoc_url="/api/v1/redoc",
    )

    # Include routers
    app.include_router(user_controller.router, prefix="/api/v1/users", tags=["Users"])
    app.include_router(item_controller.router, prefix="/api/v1/items")

    return app

app = create_app()
