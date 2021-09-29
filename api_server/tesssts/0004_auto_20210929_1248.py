# Generated by Django 3.2.7 on 2021-09-29 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_server', '0003_auto_20210929_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesstoken',
            name='cqrs_revision',
            field=models.IntegerField(default=0, help_text="This field must be incremented on any model update. It's used to for CQRS sync."),
        ),
        migrations.AlterField(
            model_name='accesstoken',
            name='cqrs_updated',
            field=models.DateTimeField(auto_now=True, help_text="This field must be incremented on every model update. It's used to for CQRS sync."),
        ),
        migrations.AlterField(
            model_name='application',
            name='cqrs_revision',
            field=models.IntegerField(default=0, help_text="This field must be incremented on any model update. It's used to for CQRS sync."),
        ),
        migrations.AlterField(
            model_name='application',
            name='cqrs_updated',
            field=models.DateTimeField(auto_now=True, help_text="This field must be incremented on every model update. It's used to for CQRS sync."),
        ),
        migrations.AlterField(
            model_name='employee',
            name='cqrs_revision',
            field=models.IntegerField(default=0, help_text="This field must be incremented on any model update. It's used to for CQRS sync."),
        ),
        migrations.AlterField(
            model_name='employee',
            name='cqrs_updated',
            field=models.DateTimeField(auto_now=True, help_text="This field must be incremented on every model update. It's used to for CQRS sync."),
        ),
        migrations.AlterField(
            model_name='grant',
            name='cqrs_revision',
            field=models.IntegerField(default=0, help_text="This field must be incremented on any model update. It's used to for CQRS sync."),
        ),
        migrations.AlterField(
            model_name='grant',
            name='cqrs_updated',
            field=models.DateTimeField(auto_now=True, help_text="This field must be incremented on every model update. It's used to for CQRS sync."),
        ),
        migrations.AlterField(
            model_name='idtoken',
            name='cqrs_revision',
            field=models.IntegerField(default=0, help_text="This field must be incremented on any model update. It's used to for CQRS sync."),
        ),
        migrations.AlterField(
            model_name='idtoken',
            name='cqrs_updated',
            field=models.DateTimeField(auto_now=True, help_text="This field must be incremented on every model update. It's used to for CQRS sync."),
        ),
        migrations.AlterField(
            model_name='refreshtoken',
            name='cqrs_revision',
            field=models.IntegerField(default=0, help_text="This field must be incremented on any model update. It's used to for CQRS sync."),
        ),
        migrations.AlterField(
            model_name='refreshtoken',
            name='cqrs_updated',
            field=models.DateTimeField(auto_now=True, help_text="This field must be incremented on every model update. It's used to for CQRS sync."),
        ),
        migrations.AlterField(
            model_name='skill',
            name='cqrs_revision',
            field=models.IntegerField(default=0, help_text="This field must be incremented on any model update. It's used to for CQRS sync."),
        ),
        migrations.AlterField(
            model_name='skill',
            name='cqrs_updated',
            field=models.DateTimeField(auto_now=True, help_text="This field must be incremented on every model update. It's used to for CQRS sync."),
        ),
        migrations.AlterField(
            model_name='skillcategories',
            name='cqrs_revision',
            field=models.IntegerField(default=0, help_text="This field must be incremented on any model update. It's used to for CQRS sync."),
        ),
        migrations.AlterField(
            model_name='skillcategories',
            name='cqrs_updated',
            field=models.DateTimeField(auto_now=True, help_text="This field must be incremented on every model update. It's used to for CQRS sync."),
        ),
        migrations.AlterField(
            model_name='skillcategory',
            name='cqrs_revision',
            field=models.IntegerField(default=0, help_text="This field must be incremented on any model update. It's used to for CQRS sync."),
        ),
        migrations.AlterField(
            model_name='skillcategory',
            name='cqrs_updated',
            field=models.DateTimeField(auto_now=True, help_text="This field must be incremented on every model update. It's used to for CQRS sync."),
        ),
        migrations.AlterField(
            model_name='skillsets',
            name='cqrs_revision',
            field=models.IntegerField(default=0, help_text="This field must be incremented on any model update. It's used to for CQRS sync."),
        ),
        migrations.AlterField(
            model_name='skillsets',
            name='cqrs_updated',
            field=models.DateTimeField(auto_now=True, help_text="This field must be incremented on every model update. It's used to for CQRS sync."),
        ),
    ]
