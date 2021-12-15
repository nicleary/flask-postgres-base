from binascii import hexlify, unhexlify
import hashlib
from os import urandom
from db.models import User
from util.cred_handler import get_secret
from db.db_utils import get_or_create, get_single_object

role_to_permission = {
    'user': ['self_profile'],
    'admin': ['user_admin', 'self_profile']
}


class InvalidRoleException(Exception):
    """Invalid Role"""
    pass


class BadAuthTokenException(Exception):
    """ Raised when an invalid authentication token is passed """
    pass


def secure_string():
    return hexlify(urandom(16)).decode("ascii")


def secure_hash(token: str):
    return hashlib.pbkdf2_hmac('sha256', unhexlify(token), unhexlify(get_secret('hash_salt')), 100000).hex()


def get_serialized_user_by_token(token: str, session):
    hash = secure_hash(token=token)
    user_object = get_single_object(session, User, key_hash=hash)
    if not user_object is None:
        serialized = user_object.to_dict()
        session.close()
        return serialized
    else:
        session.close()
        raise BadAuthTokenException


def is_valid_user(token: str, session):
    hash = secure_hash(token)
    user_object = get_single_object(session, User, key_hash=hash)
    if user_object is not None:
        return True
    else:
        raise BadAuthTokenException


def get_token(request):
    """
    Get the token from the headers of a request
    :param request: request hitting endpoint
    :return: token as a string
    """
    headers = request.headers
    bearer = headers.get('Authorization')
    if bearer is None:
        return None
    return bearer.split()[1]


def does_user_have_permission(user: User, permission: str):
    role = user.role
    if permission in role_to_permission[role]:
        return True
    else:
        return False


def create_user(username: str, email: str, role: str, session):
    if role not in role_to_permission.keys():
        raise InvalidRoleException
    key = secure_string()
    print(secure_hash(key))
    user, created = get_or_create(session, User, username=username, email=email, hash=str(secure_hash(key)), role=role)
    session.commit()
    return key, user
