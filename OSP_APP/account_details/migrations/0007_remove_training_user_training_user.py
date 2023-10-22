# Generated by Django 5.0a1 on 2023-10-22 17:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_details', '0006_alter_driverlicense_emergency_permission_date_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='training',
            name='user',
        ),
        migrations.AddField(
            model_name='training',
            name='user',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]