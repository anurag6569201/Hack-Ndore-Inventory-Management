from django.db import models

class Vehicle(models.Model):
    VEHICLE_TYPES = [
        ('Excavator', 'Excavator'),
        ('Bulldozer', 'Bulldozer'),
        ('Garbage Truck', 'Garbage Truck'),
        ('Bus', 'Bus'),
        # Add more vehicle types as needed
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
