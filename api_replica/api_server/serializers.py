from rest_framework import generics, permissions, serializers, viewsets
from django.contrib.auth.models import User, Group
from api_server.models import *
# first we define the serializers
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [ 'name', 'surname', 'hiring_date','skillset','photo']

class SkillCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillCategories
        fields = ('created','created')

class SkillCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillCategory
        fields =  "__all__"
class SkillSerializer(serializers.ModelSerializer):
    categories = serializers.ListField(child=serializers.CharField())
    class Meta:
        model = Skill
        fields = '__all__' # ['name', 'description','categories']#
    def create(self, validated_data):
        skill = Skill(
            name=validated_data['name'],
            description=validated_data['description'],
        )
        skill.save()
        for val in validated_data['categories']:
            if SkillCategory.objects.filter(name=val).exists():
                skillCategory = SkillCategory.objects.get(name=val)
            else:
                skillCategory = SkillCategory(name=val)
            skillCategory.save()
            SkillCategories.objects.create(skillCategory=skillCategory,skill=skill)
        return validated_data


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','id','username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url','id', 'name']


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
