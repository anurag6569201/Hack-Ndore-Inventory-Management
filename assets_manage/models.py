from django.db import models

class Vehicle(models.Model):
    VEHICLE_TYPES = [
        ('Excavator', 'Excavator'),
        ('Bulldozer', 'Bulldozer'),
        ('Garbage Truck', 'Garbage Truck'),
        ('Bus', 'Bus'),
    ]

    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50, choices=VEHICLE_TYPES)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, unique=True)
    condition = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    purchase_date = models.DateField()
    last_service_date = models.DateField()
    next_service_due = models.DateField()

    def __str__(self):
        return f"{self.make} {self.model} ({self.type})"

class Asset(models.Model):
    STATUS_CHOICES = [
        ('Operational', 'Operational'),
        ('Under Repair', 'Under Repair'),
        ('Decommissioned', 'Decommissioned'),
    ]

    ASSET_TYPES = [
        ('Excavator', 'Excavator'),
        ('Bulldozer', 'Bulldozer'),
        ('Garbage Truck', 'Garbage Truck'),
        ('Bus', 'Bus'),
        ('Other', 'Other'),
    ]

    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50, choices=ASSET_TYPES)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, unique=True)
    condition = models.CharField(max_length=50)
    current_location = models.CharField(max_length=100)
    last_known_location = models.CharField(max_length=100)
    latitude = models.FloatField(null=True, blank=True)  # For GPS tracking
    longitude = models.FloatField(null=True, blank=True) # For GPS tracking
    location_history = models.JSONField(null=True, blank=True)
    operational_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Operational',null=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.serial_number})"
