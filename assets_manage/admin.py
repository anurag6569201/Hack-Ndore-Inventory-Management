from django.contrib import admin
from .models import Vehicle,Asset
from import_export.admin import ImportExportModelAdmin

class VehicleAdmin(ImportExportModelAdmin):
    list_display = ('id', 'type', 'make', 'model', 'serial_number', 'condition', 'location')
    search_fields = ('make', 'model', 'serial_number')
    list_filter = ('type', 'condition')

class AssetAdmin(ImportExportModelAdmin):
    list_display = ('id', 'type', 'make', 'model', 'serial_number', 'current_location', 'operational_status')
    search_fields = ('make', 'model', 'serial_number')
    list_filter = ('type', 'operational_status')

admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Asset, AssetAdmin)