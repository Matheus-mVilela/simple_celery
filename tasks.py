from Celery.celery import app


@app.task()
def helo_world():
    print("Helo World")
