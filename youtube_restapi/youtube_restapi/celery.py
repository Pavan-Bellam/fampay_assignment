import os
from youtube_restapi import tasks
from celery import Celery

print(os.listdir())
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "youtube_restapi.settings")

app = Celery("youtube_restapi")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


