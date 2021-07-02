from fastapi import FastAPI

from src.routers.health import router as health_router


def create_app():
    app = FastAPI()

    app.include_router(health_router, prefix="/health")

    return app
