from sqlalchemy.sql import ClauseElement
from db.database_connection import create_session


def get_or_create(session, model, defaults=None, **kwargs):
    instance: model = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance, False
    else:
        params = dict((k, v) for k, v in kwargs.items() if not isinstance(v, ClauseElement))
        params.update(defaults or {})
        instance: model = model(**params)
        session.add(instance)
        return instance, True


def create_single_object(session, model, defaults=None, **kwargs):
    params = dict((k, v) for k, v in kwargs.items() if not isinstance(v, ClauseElement))
    params.update(defaults or {})
    instance = model(**params)
    session.add(instance)
    return instance


def get_single_object(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    return instance


def get_multiple_objects(session, model, **kwargs):
    instances = session.query(model).filter_by(**kwargs)
    if instances is None:
        return []
    else:
        return [instance for instance in instances]
