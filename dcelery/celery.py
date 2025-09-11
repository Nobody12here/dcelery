import os

from celery import Celery

# load the django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dcelery.settings")
app = Celery("decelery")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

@app.task
def add_num():
    return
