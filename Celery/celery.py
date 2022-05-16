from celery import Celery

app = Celery(broker='amqp://guest@rabbitmq//', backend='redis://redis')
