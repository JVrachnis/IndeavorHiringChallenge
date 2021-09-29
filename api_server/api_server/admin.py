from django.contrib import admin

from api_server.models import *


class SkillSetsInline(admin.TabularInline):
    model = SkillSets
    # extra = 2 # how many rows to show

class EmployeeAdmin(admin.ModelAdmin):
    inlines = (SkillSetsInline,)

admin.site.register(Employee,EmployeeAdmin)

class SkillCategoriesInline(admin.TabularInline):
    model = SkillCategories
    # extra = 2 # how many rows to show

class SkillAdmin(admin.ModelAdmin):
    inlines = (SkillSetsInline,)

admin.site.register(Skill,SkillAdmin)



admin.site.register(SkillCategories)
admin.site.register(SkillCategory)
