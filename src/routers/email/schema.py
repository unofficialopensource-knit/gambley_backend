from typing import List

from pydantic import BaseModel
from pydantic import EmailStr


class EmailSchema(BaseModel):
    receiver: List[EmailStr]
    subject: str
    template_name: str
    template_params: dict
