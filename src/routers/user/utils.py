from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class AnalyticsMixin(Base):
    current_sign_in_on = Column(DateTime, default=datetime.utcnow)
    last_sign_in_on = Column(DateTime, default=datetime.utcnow)
    current_sign_in_ip = Column(String)
    last_sign_in_ip = Column(String)
