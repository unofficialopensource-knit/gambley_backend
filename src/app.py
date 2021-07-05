from fastapi import FastAPI

from .routers.health import router as health_router
from .routers.email import router as email_router


def create_app():
    app = FastAPI(
        title="Gambley Backend",
        description="Backend for the gambley project",
        redoc_url=None,
        openapi_tags=[
            {"name": "health", "description": "Operations related to health check"},
            {"name": "email", "description": "Operations related to sending emails"},
        ],
    )

    app.include_router(health_router, prefix="/health", tags=["health"])
    app.include_router(email_router, prefix="/api/email", tags=["email"])

    return app
