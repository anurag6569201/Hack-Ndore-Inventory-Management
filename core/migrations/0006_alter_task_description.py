# Generated by Django 5.0.7 on 2024-07-28 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_task_taskassignment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(choices=[('Sewage & Drainage', 'Sewage & Drainage'), ('Waste Management', 'Waste Management'), ('Public Transport', 'Public Transport'), ('Public Health Services', 'Public Health Services'), ('Education and Cultural', 'Education and Cultral'), ('Services', 'Services'), ('Water Treatment and Supplies', 'Water Treatment and Supplies')], max_length=60),
        ),
    ]
