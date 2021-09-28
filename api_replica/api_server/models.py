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
            user = User.objects.update_or_create(
                id=mapped_data['id'],
                password=mapped_data['password'],
                defaults=mapped_data,
            )
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
            user = User.objects.update_or_create(
                id=mapped_data['id'],
                password=mapped_data['password'],
                defaults=mapped_data,
            )
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
        self.name = mapped_data['name']
        self.user_id = user
        self.save()
        return self

class AccessToken(ReplicaMixin, AbstractAccessToken):
    CQRS_ID = 'accesstoken'
    @staticmethod
    def _handle_user(mapped_data):
        if User.objects.filter(pk=mapped_data['id']).exists():
            user=User.objects.get(pk=mapped_data['id'])
        else:
            user = User.objects.update_or_create(
                id=mapped_data['id'],
                password=mapped_data['password'],
                defaults=mapped_data,
            )
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
        self.name = mapped_data['name']
        self.user_id = user
        self.save()
        return self

class RefreshToken(ReplicaMixin, AbstractRefreshToken):
    CQRS_ID = 'refreshtoken'
    @staticmethod
    def _handle_user(mapped_data):
        if User.objects.filter(pk=mapped_data['id']).exists():
            user=User.objects.get(pk=mapped_data['id'])
        else:
            user = User.objects.update_or_create(
                id=mapped_data['id'],
                password=mapped_data['password'],
                defaults=mapped_data,
            )
        return user
    @staticmethod
    def _handle_user(mapped_data):
        user, _ = User.objects.update_or_create(
            id=mapped_data['id'],
            defaults=mapped_data,
        )
        return user
    @classmethod
    def cqrs_create(cls, sync, mapped_data, previous_data=None):
        user = cls._handle_user(mapped_data['user'])
        return RefreshToken.objects.create(
            id=mapped_data['id'],
            user=user,
            token=mapped_data['token'],
            application=Application.objects.get(pk=mapped_data['application']),
            access_token=AccessToken.objects.get(pk=mapped_data['access_token']),
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

class IDToken(ReplicaMixin, AbstractIDToken):
    CQRS_ID = 'idtoken'
    @staticmethod
    def _handle_user(mapped_data):
        if User.objects.filter(pk=mapped_data['id']).exists():
            user=User.objects.get(pk=mapped_data['id'])
        else:
            user = User.objects.update_or_create(
                id=mapped_data['id'],
                password=mapped_data['password'],
                defaults=mapped_data,
            )
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
    class Meta:
        unique_together = ('name', 'soft_skill')

class Skill(ReplicaMixin, models.Model):
    CQRS_ID = 'skill'
    CQRS_TRACKED_FIELDS = ('name','description')

    name = models.CharField(max_length=100,primary_key=True)
    categories = models.ManyToManyField(SkillCategory)
    description = models.CharField(max_length=500)

class Employee(ReplicaMixin, models.Model):
    CQRS_ID = 'employee'
    CQRS_TRACKED_FIELDS = ('name', 'surname','hiring_date','photo')

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    hiring_date = models.DateTimeField(default=datetime.now, blank=False)
    skillset = models.ManyToManyField(Skill)
    photo = models.ImageField(upload_to='employees')
    class Meta:
        unique_together = ('name', 'surname','hiring_date')
