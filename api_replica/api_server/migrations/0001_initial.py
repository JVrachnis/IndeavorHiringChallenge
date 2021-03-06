# Generated by Django 3.2.7 on 2021-09-28 14:54

import datetime
from django.db import migrations, models
import django.utils.timezone

class Migration(migrations.Migration):

    initial = True


    run_before = [
        ('oauth2_provider', '0001_initial'),
    ]

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cqrs_revision', models.IntegerField(default=0, help_text="This field must be incremented on any model update. It's used to for CQRS sync.")),
                ('cqrs_updated', models.DateTimeField(auto_now=True, help_text="This field must be incremented on every model update. It's used to for CQRS sync.")),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cqrs_revision', models.IntegerField(default=0, help_text="This field must be incremented on any model update. It's used to for CQRS sync.")),
                ('cqrs_updated', models.DateTimeField(auto_now=True, help_text="This field must be incremented on every model update. It's used to for CQRS sync.")),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Grant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IDToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RefreshToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SkillCategory',
            fields=[
                ('cqrs_revision', models.IntegerField(default=0, help_text="This field must be incremented on any model update. It's used to for CQRS sync.")),
                ('cqrs_updated', models.DateTimeField(auto_now=True, help_text="This field must be incremented on every model update. It's used to for CQRS sync.")),
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('soft_skill', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SkillCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cqrs_revision', models.IntegerField(default=0, help_text="This field must be incremented on any model update. It's used to for CQRS sync.")),
                ('cqrs_updated', models.DateTimeField(auto_now=True, help_text="This field must be incremented on every model update. It's used to for CQRS sync.")),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('cqrs_revision', models.IntegerField(default=0, help_text="This field must be incremented on any model update. It's used to for CQRS sync.")),
                ('cqrs_updated', models.DateTimeField(auto_now=True, help_text="This field must be incremented on every model update. It's used to for CQRS sync.")),
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=500)),
                ('categories', models.ManyToManyField(through='api_server.SkillCategories',to='api_server.SkillCategory')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        # migrations.CreateModel(
        #     name='SkillCategories',
        #     fields=[
        #         ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('cqrs_revision', models.IntegerField(default=0, help_text="This field must be incremented on any model update. It's used to for CQRS sync.")),
        #         ('cqrs_updated', models.DateTimeField(auto_now=True, help_text="This field must be incremented on every model update. It's used to for CQRS sync.")),
        #         ('created', models.DateTimeField(auto_now_add=True)),
        #         ('updated', models.DateTimeField(auto_now=True)),
        #         ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_server.skill')),
        #         ('skillCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_server.skillcategory')),
        #     ],
        #     options={
        #         'abstract': False,
        #     },
        # ),
        migrations.AddField(
            model_name='skillcategories',
            name='skill',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api_server.skill'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skillcategories',
            name='skillCategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api_server.skillcategory'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='SkillSets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cqrs_revision', models.IntegerField(default=0, help_text="This field must be incremented on any model update. It's used to for CQRS sync.")),
                ('cqrs_updated', models.DateTimeField(auto_now=True, help_text="This field must be incremented on every model update. It's used to for CQRS sync.")),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cqrs_revision', models.IntegerField(default=0, help_text="This field must be incremented on any model update. It's used to for CQRS sync.")),
                ('cqrs_updated', models.DateTimeField(auto_now=True, help_text="This field must be incremented on every model update. It's used to for CQRS sync.")),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('hiring_date', models.DateTimeField(default=datetime.datetime.now)),
                ('photo', models.ImageField(upload_to='employees')),
                ('skillset', models.ManyToManyField(through='api_server.SkillSets',to='api_server.Skill')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'unique_together': {('name', 'surname', 'hiring_date')},
            },
        ),
        migrations.AddField(
            model_name='skillsets',
            name='employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api_server.employee'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skillsets',
            name='skill',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api_server.skill'),
            preserve_default=False,
        ),
        # migrations.CreateModel(
        #     name='SkillSets',
        #     fields=[
        #         ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('cqrs_revision', models.IntegerField(default=0, help_text="This field must be incremented on any model update. It's used to for CQRS sync.")),
        #         ('cqrs_updated', models.DateTimeField(auto_now=True, help_text="This field must be incremented on every model update. It's used to for CQRS sync.")),
        #         ('created', models.DateTimeField(auto_now_add=True)),
        #         ('updated', models.DateTimeField(auto_now=True)),
        #         ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_server.employee')),
        #         ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_server.skill')),
        #     ],
        #     options={
        #         'abstract': False,
        #     },
        # ),
    ]
