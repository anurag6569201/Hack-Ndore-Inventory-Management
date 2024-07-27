# models.py
from django.db import models

class Problem(models.Model):
    SERIOUSNESS_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    PROBLEM_TYPE_CHOICES = [
        ('sewage', 'Sewage'),
        ('water', 'Water'),
        ('waste', 'Waste'),
        ('road', 'Road'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='problems_images/')
    seriousness = models.CharField(max_length=10, choices=SERIOUSNESS_CHOICES)
    problem_type = models.CharField(max_length=20, choices=PROBLEM_TYPE_CHOICES)

    def __str__(self):
        return self.name
