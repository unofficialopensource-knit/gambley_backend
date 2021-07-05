from fastapi import FastAPI

from .routers.health import router as health_router


def create_app():
    app = FastAPI(
        title="Gambley Backend",
        description="Backend for the gambley project",
        redoc_url=None,
        openapi_tags=[
            {"name": "health", "description": "Operations related to health check"}
        ],
    )

    app.include_router(health_router, prefix="/health", tags=["health"])

    return app
