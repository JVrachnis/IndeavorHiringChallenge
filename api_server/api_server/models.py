from django.db import models
from django.core import validators
from django.contrib.auth import models as auth_models
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from datetime import datetime
import json
import api_server.settings

class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    soft_skill = models.BooleanField(default=False)
    class Meta:
        unique_together = ('name', 'soft_skill')

class Skill(models.Model):
    name = models.CharField(max_length=100,primary_key=True)
    categories = models.ManyToManyField(SkillCategory)
    description = models.CharField(max_length=500)

class Employee(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    hiring_date = models.DateTimeField(default=datetime.now, blank=False)
    skillset = models.ManyToManyField(Skill)
    photo = models.ImageField(upload_to='employees')
    class Meta:
        unique_together = ('name', 'surname','hiring_date')
