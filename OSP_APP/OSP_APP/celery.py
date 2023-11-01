from __future__ import absolute_import, unicode_literals
import os
from datetime import timedelta

from celery import Celery
from celery.schedules import crontab
from OSP_APP import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OSP_APP.settings')

app = Celery('OSP_APP')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

#TODO na sprawdzenie dzialania ustawiono 1 minuta
app.conf.beat_schedule = {
    'vehicle_sms_reminder': {
        'task': 'fire_vehicle.tasks.vehicle_sms_reminder',
        'schedule': timedelta(hours=24),
    },
    'driver_sms_reminder': {
        'task': 'account_details.tasks.driver_sms_reminder',
        'schedule': timedelta(hours=24),
    },
    'medical_sms_reminder': {
        'task': 'account_details.tasks.medical_sms_reminder',
        'schedule': timedelta(hours=24),
    },
    'smokebox_sms_reminder': {
        'task': 'account_details.tasks.smokebox_sms_reminder',
        'schedule': timedelta(hours=24),
    },
}

#celery -A OSP_APP worker -l info || celery -A OSP_APP beat -l info

