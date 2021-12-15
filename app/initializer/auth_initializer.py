from db.db_utils import get_single_object
from db.database_connection import create_session, initialize
from util.cred_handler import get_secret
from db.models import User
import db.schemas as schemas
from authorization.auth_utils import create_user


def check_create_single_admin():
    if get_secret('initial_admin_email') is None or get_secret('initial_admin_username') is None or \
            get_secret('hash_salt') is None:
        print('Please verify that your cred.json file is set up properly! See docs!')
        exit(1)
    initialize()
    session = create_session()
    admin_object = get_single_object(session, User, username=get_secret('initial_admin_username'),
                                     email=get_secret('initial_admin_email'), role='admin')
    if admin_object is None:
        key, user_object = create_user(get_secret('initial_admin_username'), get_secret('initial_admin_email'),
                                       'admin', session)
        print('Initial Admin User generated with details: {0}'.format(str(schemas.NewUserResponse(key=key,
                                                                                                  user=schemas.User.
                                                                                                  from_orm(
                                                                                                      user_object)))))
    else:
        print('Initial Admin User already created')
    session.close()
