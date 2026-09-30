import time
from celery import Celery

app = Celery(
    "celery_app",
    broker="amqp://guest:guest@localhost//",
    backend="db+sqlite:///result.sqlite3"
)


@app.task
def send_email(user_id: int):
    time.sleep(2)
    return f"Email sent to {user_id}"


@app.task
def cost_value(cost: int, value: int):
    time.sleep(3)
    return cost * value