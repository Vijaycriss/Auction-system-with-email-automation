from __future__ import absolute_import, unicode_literals
import os
from config.env import env
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.django.local')

app = Celery('bid_app')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')