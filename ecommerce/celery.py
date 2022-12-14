import os

from celery import Celery
from celery.schedules import crontab


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')

app = Celery('ecommerce')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# CELERY BEAT SETTINGS
app.conf.beat_schedule = {
    'send-email-every-day-at-8': {
        'task': 'schedule.tasks.send_email',
        'schedule': crontab(hour=15, minute=49),
    },
    'get_notification': {
        'task': 'schedule.tasks.get_notification',
        'schedule': 10.0,
    },
    'super_sales': {
        'task': 'schedule.tasks.super_sales',
        'schedule': crontab(hour=11, minute=0),
    },
    'reset_product': {
        'task': 'schedule.tasks.reset_product',
        'schedule': crontab(hour=11, minute=2),
    },
    'get_api_currency': {
        'task': 'schedule.tasks.get_api_currency',
        'schedule': 10,
    },
}


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
