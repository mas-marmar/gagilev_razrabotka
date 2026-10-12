from celery import Celery
from time import sleep

from datetime import datetime, timedelta
from celery.schedules import crontab


app = Celery(
    "celery_app",
    broker="amqp://guest@localhost//",
    backend="db+sqlite:///result.sqlite3"
)

app.conf.update(
    timezone="UTC",
    time_track_started=True,
    task_acks_late=True
)


@app.task
def add(x, y):
    print(f"Сумма {x + y}")

@app.task
def add(x, y):
    print(f"Отправка письма")

@app.task
def add(x, y):
    print(f"Тест")

app.conf.beat_schedule = {
    "schedul.add": {
        "task": "schedul.add",
        # "schedule": crontab(hour="", minute="", day_of_week="", month="")
        "schedule": crontab(hour="18", minute="30")
    },
    "daily": {
        "task": "schedule_send_email",
        "schedule": crontab(hour="8", minute="0", day_of_week="0")
    }
}