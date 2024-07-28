from django.db import models
from django.utils import timezone

class MaintenanceTask(models.Model):
    machinery = models.CharField(max_length=100)
    hours_of_operation = models.IntegerField()
    description = models.TextField()
    status = models.CharField(max_length=1) 
    due_date = models.DateTimeField()

    def should_send_alert(self):
        return self.due_date.date() == timezone.now().date()
    