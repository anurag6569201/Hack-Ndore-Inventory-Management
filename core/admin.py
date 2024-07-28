from django.contrib import admin
from .models import Problem,BedsInventory,O2Inventory,Ambulance,StaffMember
from import_export.admin import ImportExportModelAdmin


class ProblemAdmin(ImportExportModelAdmin):
    list_display=['seriousness','name']
admin.site.register(Problem,ProblemAdmin)

class BedsAdmin(ImportExportModelAdmin):
    list_display=['location','available']
admin.site.register(BedsInventory,BedsAdmin)

class O2Admin(ImportExportModelAdmin):
    list_display=['location','capacity_liters']
admin.site.register(O2Inventory,O2Admin)

class AmbuAdmin(ImportExportModelAdmin):
    list_display=['registration_number','type']
admin.site.register(Ambulance,AmbuAdmin)

class StaffAdmin(ImportExportModelAdmin):
    list_display=['name','role','department']
admin.site.register(StaffMember,StaffAdmin)