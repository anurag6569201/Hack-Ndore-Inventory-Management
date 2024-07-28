from django.contrib import admin
from .models import MaintenanceTask

from import_export.admin import ImportExportModelAdmin


class MaintenanceTaskAdmin(ImportExportModelAdmin):
    list_display=['machinery','hours_of_operation','status']
admin.site.register(MaintenanceTask,MaintenanceTaskAdmin)