from django.contrib import admin
from .models import Problem
from import_export.admin import ImportExportModelAdmin


class ProblemAdmin(ImportExportModelAdmin):
    list_display=['seriousness','name']

admin.site.register(Problem,ProblemAdmin)