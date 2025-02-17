# Generated by Django 5.0.7 on 2024-07-28 02:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_ambulance_bedsinventory_o2inventory_staffmember'),
    ]

    operations = [
        migrations.CreateModel(
            name='Labor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent')], max_length=10)),
                ('labor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.labor')),
            ],
        ),
    ]
