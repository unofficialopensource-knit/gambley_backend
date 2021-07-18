from fastapi_mail import FastMail
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.settings import AppConfig
from config.settings import mail_config


def db_factory():
    _engine = create_engine(AppConfig.SQLALCHEMY_DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=_engine)

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


fast_mail = FastMail(mail_config)
