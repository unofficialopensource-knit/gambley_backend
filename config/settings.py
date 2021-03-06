from os import getenv

from fastapi_mail import ConnectionConfig


mail_config = ConnectionConfig(
    MAIL_USERNAME=getenv("MAIL_USERNAME", "test_user"),
    MAIL_PASSWORD=getenv("MAIL_PASSWORD", "test_password"),
    MAIL_FROM="admin@rinnegan.io",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_FROM_NAME="Rinnegan Admin",
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
    TEMPLATE_FOLDER="templates",
    SUPPRESS_SEND=getenv("SUPPRESS_SEND", 0),
)
