from fastapi import APIRouter
from fastapi import BackgroundTasks
from fastapi.responses import UJSONResponse
from fastapi_mail import MessageSchema

from ...dependencies import fast_mail
from .models import Email


router = APIRouter()


@router.post("/new", response_class=UJSONResponse, status_code=202)
async def send_email(background_task: BackgroundTasks, email: Email) -> UJSONResponse:
    request_body = email.dict()

    message = MessageSchema(
        subject=request_body.get("subject"),
        recipients=request_body.get("receiver"),
        subtype="html",
        template_body=request_body.get("template_params"),
    )
    background_task.add_task(
        fast_mail.send_message, message, template_name=request_body.get("template_name")
    )

    return UJSONResponse(
        status_code=202,
        content={
            "message": "Sending email in background",
            "receiver": request_body.get("receiver"),
        },
    )
