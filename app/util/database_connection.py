from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from objects import Base
from cred_handler import get_secret


def create_session():
    """
    Creates a session in the database for the program
    :return: a session variable
    """
    engine = create_engine(get_secret('connection_string'))
    Base.metadata.bind = engine
    DB_session = sessionmaker(bind=engine)
    session = DB_session()
    return session