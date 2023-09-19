from celery import Celery
from dotenv import load_dotenv

load_dotenv()

app = Celery('celery_main',
             broker='amqp://',
             backend='rpc://',
             include=['tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
)

if __name__ == '__main__':
    app.start()