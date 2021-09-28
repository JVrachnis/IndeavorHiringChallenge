from rest_framework import generics, permissions, serializers, viewsets
from django.contrib.auth.models import User, Group
from api_server.models import *

from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
# first we define the serializers
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )


        user.set_password(validated_data['password'])
        user.save()

        return user

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = [ 'name', 'surname', 'hiring_date','skillset','photo']

class SkillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Skill
        fields = ['name', 'categories', 'description']

class SkillCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SkillCategory
        fields = ['name', 'soft_skill']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = [ 'name']

class ApplicationSerializer:
    """
        Simple serializer
    """
    def __init__(self, instance):
        self.instance = instance

    @property
    def data(self):
        return {
            'id': self.instance.id,
            'client_id': self.instance.client_id,
            'user': {
                'id': self.instance.user.id,
                'username': self.instance.user.username,
                'password': self.instance.user.password,
            },
            'redirect_uris': self.instance.redirect_uris,
            'client_type': self.instance.client_type,
            'authorization_grant_type': self.instance.authorization_grant_type,
            'client_secret': self.instance.client_secret,
            'name': self.instance.name,
            'skip_authorization': self.instance.skip_authorization,
            'created': self.instance.created.timestamp(),
            'updated': self.instance.updated.timestamp(),
            'algorithm': self.instance.algorithm,
            'CQRS_ID': self.instance.CQRS_ID,
        }
class AccessTokenSerializer:
    """
        Simple serializer
    """
    def __init__(self, instance):
        self.instance = instance

    @property
    def data(self):
        return {
            'id': self.instance.id,
            'user': {
                'id': self.instance.user.id,
                'username': self.instance.user.username,
                'password': self.instance.user.password,
            },
            'source_refresh_token': self.instance.source_refresh_token,
            'token': self.instance.token,
            'id_token': self.instance.id_token,
            'application': self.instance.application.id,
            'expires': self.instance.expires.timestamp(),
            'scope': self.instance.scope,
            'created': self.instance.created.timestamp(),
            'updated': self.instance.updated.timestamp(),
            'CQRS_ID': self.instance.CQRS_ID,
        }
class RefreshTokenSerializer:
    """
        Simple serializer
    """
    def __init__(self, instance):
        self.instance = instance

    @property
    def data(self):
        return {
            'id': self.instance.id,
            'user': {
                'id': self.instance.user.id,
                'username': self.instance.user.username,
                'password': self.instance.user.password,
            },
            'token': self.instance.token,
            'application': self.instance.application.id,
            'access_token': self.instance.access_token.id,
            # 'expires': self.instance.expires.timestamp(),
            # 'scope': self.instance.scope,
            'created': self.instance.created.timestamp(),
            'updated': self.instance.updated.timestamp(),
            'CQRS_ID': self.instance.CQRS_ID,
        }
class IDTokenSerializer:
    """
        Simple serializer
    """
    def __init__(self, instance):
        self.instance = instance

    @property
    def data(self):
        return {
            'id': self.instance.id,
            'user': {
                'id': self.instance.user.id,
                'username': self.instance.user.username,
                'password': self.instance.user.password,
            },
            'jti': self.instance.jti,
            'application': self.instance.application,
            'authorization_grant_type': self.instance.authorization_grant_type,
            'expires': self.instance.expires.timestamp(),
            'scope': self.instance.scope,
            'created': self.instance.created.timestamp(),
            'updated': self.instance.updated.timestamp(),
            'CQRS_ID': self.instance.CQRS_ID,
        }
