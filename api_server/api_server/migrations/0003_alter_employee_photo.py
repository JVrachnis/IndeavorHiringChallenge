# Generated by Django 3.2.7 on 2021-09-30 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_server', '0002_OAuth_model_overide'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(null=True, upload_to='employees'),
        ),
    ]