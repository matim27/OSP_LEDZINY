# Generated by Django 5.0a1 on 2023-10-18 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_details', '0002_alter_training_training_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='training_name',
            field=models.CharField(max_length=100),
        ),
    ]
