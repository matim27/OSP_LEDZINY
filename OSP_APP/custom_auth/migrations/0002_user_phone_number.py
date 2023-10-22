# Generated by Django 5.0a1 on 2023-10-17 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.PositiveIntegerField(default=123456789, max_length=9, unique=True),
            preserve_default=False,
        ),
    ]
