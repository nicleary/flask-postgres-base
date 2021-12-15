# Pydantic schemas which correspond to SQLAlchemy Models are defined here
from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):
    username: str
    email: str
    role: str
    created: datetime
    updated: datetime

    class Config:
        orm_mode = True


class NewUserResponse(BaseModel):
    token: str
    user: User
