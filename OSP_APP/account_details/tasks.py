from celery import shared_task
from django.contrib.auth import get_user_model
from datetime import date, timedelta
from account_details.models import DriverLicense, MedicalCheckup
from fire_vehicle.tasks import send_sms


UserModel = get_user_model()
today = date.today()
one_month_later = today + timedelta(days=30)


@shared_task
def driver_sms_reminder():

    driver_permission_ending = DriverLicense.objects.filter(permission_date__lte=one_month_later)
    driver_emergency_permission_ending = DriverLicense.objects.filter(emergency_permission_date__lte=one_month_later)

    for driver_user in driver_permission_ending:
        recipient_number = str(driver_user.user.phone_number)
        message = f"Data ważności twojego prawojazdy kategorii: {driver_user.category} kończy sie w dniu {driver_user.permission_date}"
        send_sms(recipient_number, message)
        print('permission-date message sent')

    for driver_user in driver_emergency_permission_ending:
        recipient_number = str(driver_user.user.phone_number)
        message = f"Data ważności pozwolenia na pojazdy uprzywilejowane kończy sie w dniu {driver_user.emergency_permission_date}"
        send_sms(recipient_number, message)
        print('emergency-date message sent')


@shared_task
def medical_sms_reminder():

    medical_checkup_ending = MedicalCheckup.objects.filter(date__lte=one_month_later)

    for medical_user in medical_checkup_ending:
        recipient_number = str(medical_user.user.phone_number)
        message = f"Ważnośc twoich badań w OSP kończy się w dniu {medical_user.date}"
        send_sms(recipient_number, message)
        print('medical-date message sent')


@shared_task
def smokebox_sms_reminder():
    smokebox_ending = MedicalCheckup.objects.filter(date__lte=one_month_later)

    for smokebox_user in smokebox_ending:
        recipient_number = str(smokebox_user.user.phone_number)
        message = f"Ważnośc komory dymowej kończy się w dniu {smokebox_user.date}"
        send_sms(recipient_number, message)
        print('smokebox-date message sent')

