from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from core.forms import ProblemForm
from django.views.decorators.csrf import csrf_exempt
import json
from core.LLM_Model.test import get_response
from core.models import Problem,BedsInventory,O2Inventory,Ambulance,StaffMember,TaskAssignment,Task

from .models import Attendance, Labor
from .forms import AttendanceForm,TaskAssignmentForm
from django.utils import timezone
@login_required
def check(request):
    return redirect("core:user_index")


@login_required
def welcome(request):
    context={

    }
    return render(request,'core/app/welcome.html',context)

@login_required
def user_index(request):
    form = ProblemForm()
    if request.method == 'POST':
        form = ProblemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('core:user_form_success')
    else:
        form = ProblemForm()
    context={
        "form": form,
    }
    return render(request,'core/app/user_index.html',context)

@login_required
def user_form_success(request):
    return render(request,'core/app/user_form_success.html')

@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message', '')
        if user_message:
            response_message = get_response(user_message)
            return JsonResponse({"reply": response_message})
        return JsonResponse({"reply": "I didn't understand that. Could you please rephrase?"})
    return JsonResponse({"error": "Invalid request method."}, status=405)

def query(request):
    public_problem=Problem.objects.all()
    context={
        'public_problem':public_problem
    }
    return render(request,'core/app/queries.html',context)


@login_required
def health(request):
    context={

    }
    return render(request,'core/app/health.html',context)

@login_required
def healthbed(request):
    health_bed=BedsInventory.objects.all()
    context={
        'health_bed':health_bed
    }
    return render(request,'core/app/beds.html',context)

@login_required
def healthambu(request):
    health_ambu=Ambulance.objects.all()
    context={
        'health_ambu':health_ambu
    }
    return render(request,'core/app/ambu.html',context)

@login_required
def healthstaff(request):
    health_staff=StaffMember.objects.all()
    context={
        'health_staff':health_staff
    }
    return render(request,'core/app/staff.html',context)

@login_required
def healtho2(request):
    health_o2=O2Inventory.objects.all()
    context={
        'health_o2':health_o2
    }
    return render(request,'core/app/o2.html',context)



# workforce
@login_required
def workforce(request):
    attendance_records = Attendance.objects.all()
    context={
        'attendance_records': attendance_records
    }
    return render(request,'core/app/workforce.html',context)

@login_required
def add_labor(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Labor.objects.create(name=name)
            return redirect('core:workforce')
    return render(request, 'core/app/add_workforce.html')

@login_required
def mark_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            date_today = timezone.now().date()
            labor = form.cleaned_data['labor']
            if Attendance.objects.filter(labor=labor, date=date_today).exists():
                return redirect('core:workforce')
            attendance = form.save(commit=False)
            attendance.date = date_today
            attendance.save()
            return redirect('core:workforce')
    else:
        form = AttendanceForm()
    return render(request, 'core/app/mark_attendance.html', {'form': form})


# task assignment

def task_assignments(request):
    public_problem=Problem.objects.all()
    tasks = Task.objects.all()
    assignments = TaskAssignment.objects.select_related('labor', 'task').all()
    return render(request, 'core/app/task_assignments.html', {'assignments': assignments,'tasks': tasks,'public_problem':public_problem})

def assign_task(request):
    if request.method == 'POST':
        form = TaskAssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:task_assignments')  # Redirect to a view that lists task assignments
    else:
        form = TaskAssignmentForm()

    return render(request, 'core/app/assign_task.html', {'form': form})