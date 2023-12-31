# Generated by Django 5.0a1 on 2023-10-28 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FireVehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('shortcut', models.CharField(max_length=100)),
                ('code_name', models.CharField(max_length=100)),
                ('license_category', models.CharField(choices=[('B', 'B'), ('C', 'C'), ('C+E', 'C+E')], max_length=3)),
                ('inspection_date', models.DateField(blank=True, null=True)),
                ('insurance_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
