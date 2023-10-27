from celery import shared_task
from django.contrib.auth import get_user_model
from twilio.rest import Client
from datetime import date, timedelta
from OSP_APP import settings
from fire_vehicle.models import FireVehicle

UserModel = get_user_model()


@shared_task
def vehicle_sms_reminder():
    today = date.today()
    one_month_later = today + timedelta(days=30)
    staff_users = UserModel.objects.filter(is_staff=True)

    vehicle_insurance_ending = FireVehicle.objects.filter(insurance_date__lte=one_month_later)
    vehicle_inspection_ending = FireVehicle.objects.filter(inspection_date__lte=one_month_later)

    for user in staff_users:
        for vehicle_insurance in vehicle_insurance_ending:
            recipient_number = str(user.phone_number)
            message = f"Ubezpieczenie konczy sie dla {vehicle_insurance.name}. W dniu {vehicle_insurance.insurance_date}"
            send_sms(recipient_number, message)
            print('Insurance message sent')

        for vehicle_inspection in vehicle_inspection_ending:
            recipient_number = str(user.phone_number)
            message = f"Data ważności przeglądu dla pojazdu {vehicle_inspection.name}. kończy sie w dniu {vehicle_inspection.insurance_date}"
            send_sms(recipient_number, message)
            print('Inspection message sent')


def send_sms(recipient_number, message):
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    from_number = settings.TWILIO_PHONE_NUMBER

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message,
        from_=from_number,
        to=recipient_number
    )


#TODO spradzenie działania (redis-server, celery | celery -A OSP_APP worker -l info)
