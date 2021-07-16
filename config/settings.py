from os import getenv

from fastapi_mail import ConnectionConfig


mail_config = ConnectionConfig(
    MAIL_USERNAME=getenv("GAMBLEY_MAIL_USERNAME"),
    MAIL_PASSWORD=getenv("GAMBLEY_MAIL_PASSWORD"),
    MAIL_FROM="admin@rinnegan.io",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_FROM_NAME="Rinnegan Admin",
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
    TEMPLATE_FOLDER="templates",
    SUPPRESS_SEND=getenv("GAMBLEY_SUPRESS_SEND", 0)
)


class ServiceConfig:
    SQLALCHEMY_DATABASE_URL = getenv("GAMBLEY_DATABASE_URL")
