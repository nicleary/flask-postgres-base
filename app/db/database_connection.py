from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base
from util.cred_handler import get_secret

engine = None


def initialize():
    engine = create_engine(get_secret('connection_string'), pool_pre_ping=True)
    Base.metadata.bind = engine


def create_session():
    """
    Creates a session in the database for the program
    :return: a session variable
    """
    DB_session = sessionmaker(bind=engine)
    session = DB_session()
    return session
