from django.contrib import admin

from api_server.models import *

admin.site.register(Employee)
admin.site.register(SkillSets)

admin.site.register(Skill)
admin.site.register(SkillCategories)
admin.site.register(SkillCategory)
