from pydantic import BaseModel


class Email(BaseModel):
    sender: str
    receiver: str
    subject: str
    template_id: int
    template_params: dict
