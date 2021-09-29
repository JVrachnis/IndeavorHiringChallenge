from django.db import models
from django.core import validators
from django.contrib.auth import models as auth_models
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from datetime import datetime
import json
import api_server.settings

from dj_cqrs.mixins import MasterMixin

from django.conf import settings

from oauth2_provider.models import (
    AbstractApplication, AbstractGrant,
    AbstractAccessToken, AbstractRefreshToken,
    AbstractIDToken,
)

class Application(MasterMixin, AbstractApplication):
    CQRS_ID = 'application'
    CQRS_SERIALIZER = 'api_server.serializers.ApplicationSerializer'
    @classmethod
    def relate_cqrs_serialization(cls, queryset):
        return queryset.select_related('user')

class Grant(MasterMixin, AbstractGrant):
    CQRS_ID = 'grant'
    CQRS_SERIALIZER = 'api_server.serializers.GrantTokenSerializer'
    @classmethod
    def relate_cqrs_serialization(cls, queryset):
        return queryset.select_related('user')

class AccessToken(MasterMixin, AbstractAccessToken):
    CQRS_ID = 'accesstoken'
    CQRS_SERIALIZER = 'api_server.serializers.AccessTokenSerializer'
    @classmethod
    def relate_cqrs_serialization(cls, queryset):
        return queryset.select_related('user')

class RefreshToken(MasterMixin, AbstractRefreshToken):
    CQRS_ID = 'refreshtoken'
    CQRS_SERIALIZER = 'api_server.serializers.RefreshTokenSerializer'
    @classmethod
    def relate_cqrs_serialization(cls, queryset):
        return queryset.select_related('user')

class IDToken(MasterMixin, AbstractIDToken):
    CQRS_ID = 'idtoken'
    CQRS_SERIALIZER = 'api_server.serializers.IDTokenSerializer'
    @classmethod
    def relate_cqrs_serialization(cls, queryset):
        return queryset.select_related('user')

class SkillCategory(MasterMixin, models.Model):
    CQRS_ID = 'skillcategory'
    CQRS_TRACKED_FIELDS = ('name', 'soft_skill')

    name = models.CharField(max_length=100)
    soft_skill = models.BooleanField(default=False)
    class Meta:
        unique_together = ('name', 'soft_skill')

class Skill(MasterMixin, models.Model):
    CQRS_ID = 'skill'
    CQRS_TRACKED_FIELDS = ('name','description')

    name = models.CharField(max_length=100,primary_key=True)
    categories = models.ManyToManyField(SkillCategory)
    description = models.CharField(max_length=500)

class Employee(MasterMixin, models.Model):
    CQRS_ID = 'employee'
    CQRS_TRACKED_FIELDS = ('name', 'surname','hiring_date','photo')
    CQRS_SERIALIZER = 'api_server.serializers.CQRSEmployeeSerializer'
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    hiring_date = models.DateTimeField(default=datetime.now, blank=False)
    skillset = models.ManyToManyField(Skill)
    photo = models.ImageField(upload_to='employees')
    class Meta:
        unique_together = ('name', 'surname','hiring_date')
