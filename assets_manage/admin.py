from django.contrib import admin
from .models import Vehicle,Asset
from import_export.admin import ImportExportModelAdmin

class VehicleAdmin(ImportExportModelAdmin):
    list_display = ('id', 'type', 'make', 'model', 'serial_number', 'condition', 'location', 'purchase_date', 'last_service_date', 'next_service_due')
    list_filter = ('type', 'condition', 'location')
    search_fields = ('make', 'model', 'serial_number')
    ordering = ('type', 'make', 'model')
    readonly_fields = ('purchase_date', 'last_service_date', 'next_service_due')  # Optional: Set fields to read-only if needed

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('type',)
        return self.readonly_fields

admin.site.register(Vehicle, VehicleAdmin)


class AssetAdmin(ImportExportModelAdmin):
    list_display = ('id', 'type', 'make', 'model', 'serial_number', 'condition', 'current_location', 'last_known_location', 'latitude', 'longitude')
    list_filter = ('type', 'condition', 'current_location')
    search_fields = ('make', 'model', 'serial_number')
    ordering = ('id',)
    fields = ('type', 'make', 'model', 'serial_number', 'condition', 'current_location', 'last_known_location', 'latitude', 'longitude')

admin.site.register(Asset, AssetAdmin)