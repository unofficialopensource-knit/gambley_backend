from fastapi_mail import FastMail

from config.settings import mail_config


fast_mail = FastMail(mail_config)
