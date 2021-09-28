from rest_framework import generics, permissions, serializers, viewsets
from django.contrib.auth.models import User, Group
from api_server.models import *
# first we define the serializers
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
