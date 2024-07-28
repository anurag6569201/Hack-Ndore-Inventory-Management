from django.db import models

class Problem(models.Model):
    SERIOUSNESS_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    PROBLEM_TYPE_CHOICES = [
        ('Sewage & Drainage', 'Sewage & Drainage'),
        ('Waste Management', 'Waste Management'),
        ('Public Transport', 'Public Transport'),
        ('Public Health Services', 'Public Health Services'),
        ('Education and Cultural', 'Education and Cultral'),
        ('Services', 'Services'),
        ('Water Treatment and Supplies', 'Water Treatment and Supplies'),
    ]

    STATUS_CHOICES = [
        ('not_seen', 'Not Seen'),
        ('seen', 'Seen'),
        ('action_taken', 'Action Taken'),
        ('solved', 'Solved'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='problems_images/')
    seriousness = models.CharField(max_length=60, choices=SERIOUSNESS_CHOICES)
    problem_type = models.CharField(max_length=60, choices=PROBLEM_TYPE_CHOICES)
    status = models.CharField(max_length=60, choices=STATUS_CHOICES, default='not_seen')

    def __str__(self):
        return self.name


class BedsInventory(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()
    available = models.IntegerField()
    condition = models.CharField(max_length=255)
    last_checked = models.DateField()

    def __str__(self):
        return f"ID: {self.id} - Location: {self.location}"
    

class O2Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=255)
    capacity_liters = models.IntegerField()
    available = models.IntegerField()
    condition = models.CharField(max_length=255)
    last_checked = models.DateField()

    def __str__(self):
        return f"ID: {self.id} - Location: {self.location}"
    
class Ambulance(models.Model):
    id = models.AutoField(primary_key=True)
    registration_number = models.CharField(max_length=255, unique=True)
    type = models.CharField(max_length=255)
    available = models.BooleanField()
    condition = models.CharField(max_length=255)
    last_maintenance = models.DateField()

    def __str__(self):
        return f"ID: {self.id} - Registration Number: {self.registration_number}"
    
class StaffMember(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    last_updated = models.DateField()

    def __str__(self):
        return f"ID: {self.id} - Name: {self.name} - Role: {self.role}"
    

# attendence systems

class Labor(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    labor = models.ForeignKey(Labor, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    def __str__(self):
        return f'{self.labor} - {self.date} - {self.status}'
    

# task assign
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=60, choices=Problem.PROBLEM_TYPE_CHOICES)

    def __str__(self):
        return self.title

class TaskAssignment(models.Model):
    labor = models.ForeignKey(Labor, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    date_assigned = models.DateField()
    status = models.CharField(max_length=10)  # e.g., 'Completed', 'Pending'

    def __str__(self):
        return f'{self.labor.name} - {self.task.title} - {self.date_assigned} - {self.status}'