from fastapi import APIRouter
from fastapi.responses import UJSONResponse

from .models import Email


router = APIRouter()


@router.post("/new", response_class=UJSONResponse, status_code=201)
async def health(email: Email):
    return {"status": "healthy"}
