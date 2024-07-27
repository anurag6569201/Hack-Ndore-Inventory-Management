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
