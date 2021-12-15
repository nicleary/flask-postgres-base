from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, Float, UniqueConstraint, LargeBinary, \
    Table, DateTime, Date, Text
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()


class PrimaryKeyBase:
    id = Column(Integer, primary_key=True, autoincrement=True)


class User(Base, PrimaryKeyBase):
    __tablename__ = 'user'

    username = Column(String(length=128), unique=True, nullable=False)
    email = Column(String(length=256), unique=True, nullable=False)
    hash = Column(String(length=128), nullable=False)
    role = Column(String(length=16), nullable=False)
    created = Column(DateTime, default=datetime.now())
    updated = Column(DateTime, default=datetime.now())
