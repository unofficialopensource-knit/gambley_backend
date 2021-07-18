from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base

from .utils import AnalyticsMixin
from .utils import UpdatesMixin


Base = declarative_base()


class User(Base, AnalyticsMixin, UpdatesMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    is_active = Column(Boolean, default=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
