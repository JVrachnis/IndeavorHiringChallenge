# Generated by Django 3.2.7 on 2021-09-30 10:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_server', '0003_alter_employee_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='hiring_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
