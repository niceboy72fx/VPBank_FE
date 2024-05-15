from __future__ import absolute_import, unicode_literals

import random
import os
import subprocess, sys

from celery import Celery, shared_task

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
app = Celery("core")

app.config_from_object("django.conf:settings", namespace = "CELERY")
# app.conf.broker_connection_retry_on_startup = True
app.conf.worker_concurrency = 4


python_path = sys.executable
dir_path = os.path.dirname(python_path)
celery_path = os.path.join(dir_path, 'celery')