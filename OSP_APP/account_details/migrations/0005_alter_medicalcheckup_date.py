# Generated by Django 5.0a1 on 2023-10-18 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_details', '0004_alter_driverlicense_emergency_permission_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalcheckup',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
