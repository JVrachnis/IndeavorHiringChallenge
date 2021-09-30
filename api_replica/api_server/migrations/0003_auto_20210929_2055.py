# Generated by Django 3.2.7 on 2021-09-29 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_server', '0002_OAuth_model_overide'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesstoken',
            name='cqrs_revision',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='accesstoken',
            name='cqrs_updated',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='application',
            name='cqrs_revision',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='application',
            name='cqrs_updated',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='cqrs_revision',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='cqrs_updated',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='skill',
            name='cqrs_revision',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='skill',
            name='cqrs_updated',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='skillcategories',
            name='cqrs_revision',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='skillcategories',
            name='cqrs_updated',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='skillcategory',
            name='cqrs_revision',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='skillcategory',
            name='cqrs_updated',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='skillsets',
            name='cqrs_revision',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='skillsets',
            name='cqrs_updated',
            field=models.DateTimeField(),
        ),
    ]
