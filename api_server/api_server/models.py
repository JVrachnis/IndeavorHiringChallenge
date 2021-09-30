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
    # @classmethod
    # def relate_cqrs_serialization(cls, queryset):
    #     return queryset.select_related('user')

class Grant(AbstractGrant):
    pass
    # @classmethod
    # def relate_cqrs_serialization(cls, queryset):
    #     return queryset.select_related('user')

class AccessToken(MasterMixin, AbstractAccessToken):
    CQRS_ID = 'accesstoken'
    CQRS_SERIALIZER = 'api_server.serializers.AccessTokenSerializer'
    # @classmethod
    # def relate_cqrs_serialization(cls, queryset):
    #     return queryset.select_related('user')

class RefreshToken(AbstractRefreshToken):
    pass
    # @classmethod
    # def relate_cqrs_serialization(cls, queryset):
    #     return queryset.select_related('access_token').select_related('user')

class IDToken(AbstractIDToken):
    pass
    # @classmethod
    # def relate_cqrs_serialization(cls, queryset):
    #     return queryset.select_related('user')

class SkillCategory(MasterMixin, models.Model):
    CQRS_ID = 'skillcategory'
    CQRS_TRACKED_FIELDS = ('name', 'soft_skill')

    name = models.CharField(max_length=100,primary_key=True)
    soft_skill = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Skill(MasterMixin, models.Model):
    CQRS_ID = 'skill'
    CQRS_TRACKED_FIELDS = ('name','description')
    # CQRS_SERIALIZER = 'api_server.serializers.CQRSSkillSerializer'

    name = models.CharField(max_length=100,primary_key=True)
    categories = models.ManyToManyField(SkillCategory, through='SkillCategories')
    description = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # @classmethod
    # def relate_cqrs_serialization(cls, queryset):
    #     return queryset.select_related('skillCategory')

class SkillCategories(MasterMixin, models.Model):
    CQRS_ID = 'skillcategories'
    CQRS_TRACKED_FIELDS = ('skill','skillCategory')
    CQRS_SERIALIZER = 'api_server.serializers.CQRSSkillCategoriesSerializer'

    skill = models.ForeignKey(Skill,on_delete=models.CASCADE)
    skillCategory = models.ForeignKey(SkillCategory,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # @classmethod
    # def relate_cqrs_serialization(cls, queryset):
    #     return queryset.select_related('skill').select_related('skillCategory')

class Employee(MasterMixin, models.Model):
    CQRS_ID = 'employee'
    CQRS_TRACKED_FIELDS = ('name', 'surname','hiring_date','photo')
    CQRS_SERIALIZER = 'api_server.serializers.CQRSEmployeeSerializer'
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    hiring_date = models.DateTimeField(default=datetime.now, blank=True)
    skillset = models.ManyToManyField(Skill, through='SkillSets')
    photo = models.ImageField(upload_to='employees',null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = ('name', 'surname','hiring_date')
    # @classmethod
    # def relate_cqrs_serialization(cls, queryset):
    #     return queryset.select_related('skillset')


class SkillSets(MasterMixin, models.Model):
    CQRS_ID = 'skillsets'
    CQRS_TRACKED_FIELDS = ('skill','employee')
    CQRS_SERIALIZER = 'api_server.serializers.CQRSSkillSetsSerializer'

    skill = models.ForeignKey(Skill,on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # @classmethod
    # def relate_cqrs_serialization(cls, queryset):
    #     return queryset.select_related('employee')
