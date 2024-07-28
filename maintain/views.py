from django.utils import timezone
from django.shortcuts import render
from .models import MaintenanceTask
from .sms_utility import send_sms_alert

def maintain(request):
    context={

    }
    return render(request,'maintain/app/maintain.html',context)

def remainder(request):
    maintenance_tasks = MaintenanceTask.objects.filter(due_date__lte=timezone.now())
    future_tasks = MaintenanceTask.objects.filter(due_date__gt=timezone.now())
    # for task in maintenance_tasks:
    #     if task.should_send_alert():
    #         send_sms_alert(task)

    context={
        'maintenance_tasks': maintenance_tasks,
        'future_tasks':future_tasks,
    }
    return render(request,'maintain/app/remainder.html',context)

def view_repair_activities(request):
    repair_activities = MaintenanceTask.objects.all().order_by('due_date')
    return render(request, 'maintain/app/activity.html', {'repair_activities': repair_activities})