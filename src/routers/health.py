from fastapi import APIRouter
from fastapi.responses import UJSONResponse


router = APIRouter()


@router.get("/", response_class=UJSONResponse)
async def health():
    return {"status": "healthy"}
