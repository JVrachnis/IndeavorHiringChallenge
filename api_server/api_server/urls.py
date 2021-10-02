from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

from rest_framework import routers
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.response import Response

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

from api_server.views import *




# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)

#curl -X POST -d 'grant_type=password&username=admin&password=123qwe!@#QWE' -u"e5AnSIkaVJjTCECv28ZXmPxgDzeAjBXe4n4v63n0:kbCmhs2ExhCYOcggI8AjCzXwZHCsElHhSfE2v3cXzzMeZLJmMYFhKdA58teRY42MWAINnFOiYYoKO31nvEFUmjBJigUICDbS6gIa6WxVmIyMXmDxBSwVDoCAfOYJmCup" http://localhost:443/o/token/
router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'employees',EmployeeViewSet,basename='employee')
router.register(r'skills',SkillViewSet,basename='skill')
router.register(r'skillcategories',SkillCategoryViewSet)
# Setup the URLs and include login URLs for the browsable API.
urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/o/checkauth/',CheckAuth.as_view()),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
