from celery import Celery

app = Celery(broker="pyamqp://guest@rabbitmq//")
