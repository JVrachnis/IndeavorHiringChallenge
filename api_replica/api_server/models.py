from django.db import models
from django.core import validators
from django.contrib.auth import models as auth_models
from django.contrib.auth.models import Permission,User
from django.contrib.contenttypes.models import ContentType

from datetime import datetime
import json
import api_server.settings

from dj_cqrs.mixins import ReplicaMixin

from django.conf import settings

from oauth2_provider.models import (
    AbstractApplication, AbstractGrant,
    AbstractAccessToken, AbstractRefreshToken,
    AbstractIDToken,
)

from datetime import datetime

from django.utils.timezone import make_aware

class Application(ReplicaMixin, AbstractApplication):
    CQRS_ID = 'application'
    @staticmethod
    def _handle_user(mapped_data):
        if User.objects.filter(pk=mapped_data['id']).exists():
            user=User.objects.get(pk=mapped_data['id'])
        else:
            user = User.objects.create(id=mapped_data['id'],username=mapped_data['username'],password=mapped_data['password'])
        return user
    @classmethod
    def cqrs_create(cls, sync, mapped_data, previous_data=None):
        user = cls._handle_user(mapped_data['user'])
        return Application.objects.create(
            id=mapped_data['id'],
            client_id=mapped_data['client_id'],
            user=user,
            redirect_uris=mapped_data['redirect_uris'],
            client_type=mapped_data['client_type'],
            authorization_grant_type=mapped_data['authorization_grant_type'],
            client_secret=mapped_data['client_secret'],
            name=mapped_data['name'],
            skip_authorization=mapped_data['skip_authorization'],
            created=mapped_data['created'],
            updated=mapped_data['updated'],
            algorithm=mapped_data['algorithm'],

            cqrs_revision=mapped_data['cqrs_revision'],
            cqrs_updated=mapped_data['cqrs_updated'],
        )

    def cqrs_update(self, sync, mapped_data, previous_data=None):
        user = self._handle_user(mapped_data['user'])
        self.name = mapped_data['name']
        self.user_id = user
        self.save()
        return self
class Grant(ReplicaMixin, AbstractGrant):
    CQRS_ID = 'grant'
    @staticmethod
    def _handle_user(mapped_data):
        if User.objects.filter(pk=mapped_data['id']).exists():
            user=User.objects.get(pk=mapped_data['id'])
        else:
            user = User.objects.create(id=mapped_data['id'],username=mapped_data['username'],password=mapped_data['password'])
        return user
    @classmethod
    def cqrs_create(cls, sync, mapped_data, previous_data=None):
        user = cls._handle_user(mapped_data['user'])
        return Grant.objects.create(
            id=mapped_data['id'],
            user=user,
            code=mapped_data['code'],
            application=Application.objects.get(pk=mapped_data['application']),
            authorization_grant_type=mapped_data['authorization_grant_type'],
            expires=make_aware(datetime.fromtimestamp(mapped_data['expires'])),
            redirect_uri=mapped_data['redirect_uri'],
            scope=mapped_data['scope'],
            created=mapped_data['created'],
            updated=mapped_data['updated'],
            code_challenge=mapped_data['code_challenge'],
            code_challenge_method=mapped_data['code_challenge_method'],
            nonce=mapped_data['nonce'],
            claims=mapped_data['claims'],

            cqrs_revision=mapped_data['cqrs_revision'],
            cqrs_updated=mapped_data['cqrs_updated'],
        )

    def cqrs_update(self, sync, mapped_data, previous_data=None):
        user = self._handle_user(mapped_data['user'])
        self.id=mapped_data['id'],
        self.user=user,
        self.code=mapped_data['code'],
        self.application=Application.objects.get(pk=mapped_data['application']),
        self.authorization_grant_type=mapped_data['authorization_grant_type'],
        self.expires=make_aware(datetime.fromtimestamp(mapped_data['expires'])),
        self.redirect_uri=mapped_data['redirect_uri'],
        self.scope=mapped_data['scope'],
        self.created=mapped_data['created'],
        self.updated=mapped_data['updated'],
        self.code_challenge=mapped_data['code_challenge'],
        self.code_challenge_method=mapped_data['code_challenge_method'],
        self.nonce=mapped_data['nonce'],
        self.claims=mapped_data['claims'],

        self.cqrs_revision=mapped_data['cqrs_revision'],
        self.cqrs_updated=mapped_data['cqrs_updated'],
        self.save()
        return self

class AccessToken(ReplicaMixin, AbstractAccessToken):
    CQRS_ID = 'accesstoken'
    @staticmethod
    def _handle_user(mapped_data):
        if User.objects.filter(pk=mapped_data['id']).exists():
            user=User.objects.get(pk=mapped_data['id'])
        else:
            user = User.objects.create(id=mapped_data['id'],username=mapped_data['username'],password=mapped_data['password'])
        return user
    @classmethod
    def cqrs_create(cls, sync, mapped_data, previous_data=None):
        user = cls._handle_user(mapped_data['user'])
        return AccessToken.objects.create(
            id=mapped_data['id'],
            user=user,
            source_refresh_token=mapped_data['source_refresh_token'],
            token=mapped_data['token'],
            id_token=mapped_data['id_token'],
            application=Application.objects.get(pk=mapped_data['application']),
            expires=make_aware(datetime.fromtimestamp(mapped_data['expires'])),
            created=mapped_data['created'],
            updated=mapped_data['updated'],

            cqrs_revision=mapped_data['cqrs_revision'],
            cqrs_updated=mapped_data['cqrs_updated'],
        )

    def cqrs_update(self, sync, mapped_data, previous_data=None):
        user = self._handle_user(mapped_data['user'])
        self.id=mapped_data['id'],
        self.user=user,
        self.source_refresh_token=mapped_data['source_refresh_token'],
        self.token=mapped_data['token'],
        self.id_token=mapped_data['id_token'],
        self.application=Application.objects.get(pk=mapped_data['application']),
        self.expires=make_aware(datetime.fromtimestamp(mapped_data['expires'])),
        self.created=mapped_data['created'],
        self.updated=mapped_data['updated'],

        self.cqrs_revision=mapped_data['cqrs_revision'],
        self.cqrs_updated=mapped_data['cqrs_updated'],
        self.user = user
        self.save()
        return self

class RefreshToken(ReplicaMixin, AbstractRefreshToken):
    CQRS_ID = 'refreshtoken'
    @staticmethod
    def _handle_user(mapped_data):
        if User.objects.filter(pk=mapped_data['id']).exists():
            user=User.objects.get(pk=mapped_data['id'])
        else:
            user = User.objects.create(id=mapped_data['id'],username=mapped_data['username'],password=mapped_data['password'])
        return user
    @classmethod
    def cqrs_create(cls, sync, mapped_data, previous_data=None):
        user = cls._handle_user(mapped_data['user'])
        return RefreshToken.objects.create(
            id=mapped_data['id'],
            user=user,
            token=mapped_data['token'],
            application=Application.objects.get(pk=mapped_data['application']),
            # access_token=AccessToken.objects.get(pk=mapped_data['access_token']),
            created=mapped_data['created'],
            updated=mapped_data['updated'],

            cqrs_revision=mapped_data['cqrs_revision'],
            cqrs_updated=mapped_data['cqrs_updated'],
        )

    def cqrs_update(self, sync, mapped_data, previous_data=None):
        user = self._handle_user(mapped_data['user'])
        self.id=mapped_data['id'],
        self.user=user,
        self.token=mapped_data['token'],
        self.application=Application.objects.get(pk=mapped_data['application']),
        # self.access_token=AccessToken.objects.get(pk=mapped_data['access_token']),
        self.created=mapped_data['created'],
        self.updated=mapped_data['updated'],

        self.cqrs_revision=mapped_data['cqrs_revision'],
        self.cqrs_updated=mapped_data['cqrs_updated'],
        self.save()
        return self

class IDToken(ReplicaMixin, AbstractIDToken):
    CQRS_ID = 'idtoken'
    @staticmethod
    def _handle_user(mapped_data):
        if User.objects.filter(pk=mapped_data['id']).exists():
            user=User.objects.get(pk=mapped_data['id'])
        else:
            user = User.objects.create(id=mapped_data['id'],username=mapped_data['username'],password=mapped_data['password'])
        return user
    @classmethod
    def cqrs_create(cls, sync, mapped_data, previous_data=None):
        user = cls._handle_user(mapped_data['user'])
        return IDToken.objects.create(
            id=mapped_data['id'],
            user=user,
            jti=mapped_data['jti'],
            application=Application.objects.get(pk=mapped_data['application']),
            authorization_grant_type=mapped_data['authorization_grant_type'],
            expires=make_aware(datetime.fromtimestamp(mapped_data['expires'])),
            scope=mapped_data['scope'],
            created=mapped_data['created'],
            updated=mapped_data['updated'],

            cqrs_revision=mapped_data['cqrs_revision'],
            cqrs_updated=mapped_data['cqrs_updated'],
        )

    def cqrs_update(self, sync, mapped_data, previous_data=None):
        user = self._handle_user(mapped_data['user'])
        self.name = mapped_data['name']
        self.user_id = user
        self.save()
        return self

class SkillCategory(ReplicaMixin, models.Model):
    CQRS_ID = 'skillcategory'
    CQRS_TRACKED_FIELDS = ('name', 'soft_skill')

    name = models.CharField(max_length=100)
    soft_skill = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = ('name', 'soft_skill')

class Skill(ReplicaMixin, models.Model):
    CQRS_ID = 'skill'
    CQRS_TRACKED_FIELDS = ('name','description')

    name = models.CharField(max_length=100,primary_key=True)
    categories = models.ManyToManyField(SkillCategory, through='SkillCategories')
    description = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class SkillCategories(ReplicaMixin, models.Model):
    CQRS_ID = 'skillcategories'
    CQRS_TRACKED_FIELDS = ('skill','skillCategory')

    skill = models.ForeignKey(Skill,on_delete=models.CASCADE)
    skillCategory = models.ForeignKey(SkillCategory,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    @classmethod
    def cqrs_create(cls, sync, mapped_data, previous_data=None):
        return SkillCategories.objects.create(
            id=mapped_data['id'],
            skill=Skill.objects.get(name = mapped_data['skill']['name']),
            skillCategory= SkillCategory.objects.get(pk = mapped_data['skillCategory']['id']),
            created=mapped_data['created'],
            updated=mapped_data['updated'],

            cqrs_revision=mapped_data['cqrs_revision'],
            cqrs_updated=mapped_data['cqrs_updated'],
        )

    def cqrs_update(self, sync, mapped_data, previous_data=None):
        self.skill=Skill.objects.get(name = mapped_data['skill']['name']),
        self.skillCategory= SkillCategory.objects.get(pk = mapped_data['skillCategory']['id']),
        self.created = mapped_data['created']
        self.updated = mapped_data['updated']
        self.cqrs_revision=mapped_data['cqrs_revision'],
        self.cqrs_updated=mapped_data['cqrs_updated'],
        self.save()
        return self

class Employee(ReplicaMixin, models.Model):
    CQRS_ID = 'employee'
    CQRS_TRACKED_FIELDS = ('name', 'surname','hiring_date','photo')

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    hiring_date = models.DateTimeField(default=datetime.now, blank=False)
    skillset = models.ManyToManyField(Skill, through='SkillSets')
    photo = models.ImageField(upload_to='employees')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = ('name', 'surname','hiring_date')


class SkillSets(ReplicaMixin, models.Model):
    CQRS_ID = 'skillsets'
    CQRS_TRACKED_FIELDS = ('skill','employee')

    skill = models.ForeignKey(Skill,on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    @classmethod
    def cqrs_create(cls, sync, mapped_data, previous_data=None):
        return SkillSets.objects.create(
            id=mapped_data['id'],
            skill=Skill.objects.get(name = mapped_data['skill']['name']),
            employee= Employee.objects.get(pk = mapped_data['employee']['id']),
            created=mapped_data['created'],
            updated=mapped_data['updated'],

            cqrs_revision=mapped_data['cqrs_revision'],
            cqrs_updated=mapped_data['cqrs_updated'],
        )

    def cqrs_update(self, sync, mapped_data, previous_data=None):
        self.skill=Skill.objects.get(name = mapped_data['skill']['name']),
        self.employee= Employee.objects.get(pk = mapped_data['employee']['id']),
        self.created = mapped_data['created']
        self.updated = mapped_data['updated']
        self.cqrs_revision=mapped_data['cqrs_revision'],
        self.cqrs_updated=mapped_data['cqrs_updated'],
        self.save()
        return self
