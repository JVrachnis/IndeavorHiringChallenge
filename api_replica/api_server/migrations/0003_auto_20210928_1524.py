# Generated by Django 3.2.7 on 2021-09-28 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_server', '0002_auto_20210928_1455'),
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
            model_name='grant',
            name='code_challenge_method',
            field=models.CharField(blank=True, choices=[('plain', 'plain'), ('S256', 'S256')], default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='grant',
            name='cqrs_revision',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='grant',
            name='cqrs_updated',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='idtoken',
            name='cqrs_revision',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='idtoken',
            name='cqrs_updated',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='refreshtoken',
            name='cqrs_revision',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='refreshtoken',
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
            model_name='skillcategory',
            name='cqrs_revision',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='skillcategory',
            name='cqrs_updated',
            field=models.DateTimeField(),
        ),
    ]
