
from django.contrib.auth.models import User, Group
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers

from django.shortcuts import get_object_or_404

from rest_framework import generics, permissions, serializers, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from api_server.serializers import *
from api_server.models import *

import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class UserViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated,permissions.IsAdminUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    @method_decorator(cache_page(3))
    def list(self, *args, **kwargs):
        return super().list(*args, **kwargs)
    @method_decorator(cache_page(60))
    def retrieve(self, *args, **kwargs):
        return super().retrieve(*args, **kwargs)

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    @method_decorator(cache_page(3))
    def list(self, *args, **kwargs):
        return super().list(*args, **kwargs)
    @method_decorator(cache_page(60))
    def retrieve(self, *args, **kwargs):
        return super().retrieve(*args, **kwargs)

class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset =  Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'name', 'surname','hiring_date','skillset__name']
    search_fields = ['id','name', 'surname','hiring_date','skillset__name']
    ordering_fields = ['name','surname','hiring_date', 'id']
    ordering = ['hiring_date']

    @method_decorator(cache_page(3))
    def list(self, *args, **kwargs):
        return super().list(*args, **kwargs)
    @method_decorator(cache_page(60))
    def retrieve(self, *args, **kwargs):
        return super().retrieve(*args, **kwargs)

class SkillViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name', 'description','categories__name']
    search_fields = ['name', 'description','categories__name']
    ordering_fields = ['name','description','categories__name']
    ordering = ['name']

    @method_decorator(cache_page(3))
    def list(self, *args, **kwargs):
        return super().list(*args, **kwargs)
    @method_decorator(cache_page(60))
    def retrieve(self, *args, **kwargs):
        return super().retrieve(*args, **kwargs)

class SkillCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = SkillCategory.objects.all()
    serializer_class = SkillCategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    @method_decorator(cache_page(3))
    def list(self, *args, **kwargs):
        return super().list(*args, **kwargs)
    @method_decorator(cache_page(60))
    def retrieve(self, *args, **kwargs):
        return super().retrieve(*args, **kwargs)
