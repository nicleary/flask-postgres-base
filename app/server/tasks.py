''' Tasks related to celery functions '''
import time
import random
import datetime

from celery import Celery, current_task
from celery.exceptions import CeleryError
from celery.result import AsyncResult
from util.cred_handler import get_secret

REDIS_URL = 'redis://redis:6379/0'
BROKER_URL = 'amqp://{0}:{1}@rabbit//'.format(get_secret("RABBITMQ_USER"), get_secret("RABBITMQ_PASS"))

CELERY = Celery('tasks',
            backend=REDIS_URL,
            broker=BROKER_URL)

CELERY.conf.accept_content = ['json', 'msgpack']
CELERY.conf.result_serializer = 'msgpack'

def get_job(job_id):
    '''
    The job ID is passed and the celery job is returned.
    '''
    return AsyncResult(job_id, app=CELERY)


@CELERY.task()
def this_is_a_task():
    a = 1
    b = 2
    time.sleep(2)
    number = random.randrange(1,600)
    return a + b * number