# Generated by Django 5.0a1 on 2023-10-17 17:57

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_auth', '0002_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=9, region=None, unique=True),
        ),
    ]