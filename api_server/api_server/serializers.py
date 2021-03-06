from rest_framework import generics, permissions, serializers, viewsets
from django.contrib.auth.models import User, Group
from api_server.models import *

from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
# first we define the serializers
class RegisterSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(
    #         required=True,
    #         validators=[UniqueValidator(queryset=User.objects.all())]
    #         )

    password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({"password1": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
        )


        user.set_password(validated_data['password1'])
        user.save()

        return user

class EmployeeSerializer(serializers.ModelSerializer):
    skillset = serializers.ListField(child=serializers.CharField())
    class Meta:
        model = Employee
        fields = '__all__' # ['name', 'description','categories']#
    def create(self, validated_data):
        employee = Employee(
            name=validated_data['name'],
            surname=validated_data['surname'],
            hiring_date=validated_data['hiring_date'],
        )
        employee.save()
        print('here')
        print(validated_data)
        if 'skillset' in validated_data:
            for val in validated_data['skillset']:
                if Skill.objects.filter(name=val).exists():
                    skill = Skill.objects.get(name=val)
                else:
                    skill = Skill(name=val,description='')
                    skill.save()
                SkillSets.objects.create(employee=employee,skill=skill)
        return validated_data
    def update(self,instance,validated_data):
        employee = instance
        employee.name=validated_data.get('name', instance.name)
        employee.surname=validated_data.get('surname', instance.surname)
        employee.hiring_date=validated_data.get('hiring_date', instance.hiring_date)
        employee.save()
        SkillSets.objects.filter(employee=employee).delete()
        if 'skillset' in validated_data:
            for val in validated_data['skillset']:
                if Skill.objects.filter(name=val).exists():
                    skill = Skill.objects.get(name=val)
                else:
                    skill = Skill(name=val,description='')
                    skill.save()
                SkillSets.objects.create(employee=employee,skill=skill)
        return validated_data
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
    def update(self,instance,validated_data):
        skill = instance
        skill.description=validated_data.get('description', instance.description)
        skill.save()
        SkillCategory.objects.filter(skill=skill).delete()
        for val in validated_data['categories']:
            if SkillCategory.objects.filter(name=val).exists():
                skillCategory = SkillCategory.objects.get(name=val)
            else:
                skillCategory = SkillCategory(name=val)
            skillCategory.save()
            SkillCategories.objects.create(skillCategory=skillCategory,skill=skill)
        return validated_data
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = [ 'name']


class CQRSSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = [ 'name', 'categories', 'description','created','updated']
    """
        Simple serializer
    """
    def __init__(self, instance):
        self.instance = instance

    @property
    def data(self):
        return {
            'name': self.instance.name,
            'categories': self.instance.categories,
            'description': self.instance.description,
            'created': self.instance.created.timestamp(),
            'updated': self.instance.updated.timestamp(),
            'CQRS_ID': self.instance.CQRS_ID,
        }
class CQRSEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'surname', 'hiring_date','photo',]

# class CQRSEmployeeSerializer:
#     """
#         Simple serializer
#     """
#     def __init__(self, instance):
#         self.instance = instance
#
#     @property
#     def data(self):
#         return {
#             'id': self.instance.id,
#             'name': self.instance.name,
#             'surname': self.instance.surname,
#             'hiring_date': self.instance.hiring_date.timestamp(),
#             'skillset': {
#                 'id': self.instance.skillset.id,
#                 'skill': self.instance.skillset.urlskill.id,
#                 'employee': self.instance.skillset.employee.id,
#             },
#             'photo': self.instance.photo.url,
#             'created': self.instance.created.timestamp(),
#             'updated': self.instance.updated.timestamp(),
#             'CQRS_ID': self.instance.CQRS_ID,
#         }
class CQRSSkillCategoriesSerializer:
    """
        Simple serializer
    """
    def __init__(self, instance):
        self.instance = instance

    @property
    def data(self):
        return {
            'id': self.instance.id,
            'skill': {
                'name': self.instance.skill.name,
            },
            'skillCategory': {
                'name': self.instance.skillCategory.name,
            },
            'created': self.instance.created.timestamp(),
            'updated': self.instance.updated.timestamp(),
            'CQRS_ID': self.instance.CQRS_ID,
        }
class CQRSSkillSetsSerializer:
    """
        Simple serializer
    """
    def __init__(self, instance):
        self.instance = instance

    @property
    def data(self):
        return {
            'id': self.instance.id,
            'skill': {
                'name': self.instance.skill.name,
            },
            'employee': {
                'id': self.instance.employee.id,
            },
            'created': self.instance.created.timestamp(),
            'updated': self.instance.updated.timestamp(),
            'CQRS_ID': self.instance.CQRS_ID,
        }
class CQRSEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [ 'id', 'name', 'surname', 'hiring_date','photo','created','updated']

# class CQRSEmployeeSerializer:
#     """
#         Simple serializer
#     """
#     def __init__(self, instance):
#         self.instance = instance
#
#     @property
#     def data(self):
#         return {
#             'id': self.instance.id,
#             'name': self.instance.name,
#             'surname': self.instance.surname,
#             'hiring_date': self.instance.hiring_date.timestamp(),
#             'photo': self.instance.photo.url,
#             'created': self.instance.created.timestamp(),
#             'updated': self.instance.updated.timestamp(),
#             'CQRS_ID': self.instance.CQRS_ID,
#         }
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
