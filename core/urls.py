from core import views
from django.urls import path

app_name="core"

urlpatterns=[
    path("",views.check,name="check"),
    path("home/",views.welcome,name="welcome"),
    path("userhome/",views.user_index,name="user_index"),
    path("success/",views.user_form_success,name="user_form_success"),
    path('send-message/', views.send_message, name='send_message'),

    # queries
    path('query/', views.query, name='query'),
    path('health/', views.health, name='health'),
    path('health/bed', views.healthbed, name='healthbed'),
    path('health/staff', views.healthstaff, name='healthstaff'),
    path('health/o2', views.healtho2, name='healtho2'),
    path('health/ambu', views.healthambu, name='healthambu'),

    path('add-labor/', views.add_labor, name='add_labor'),
    path('mark-attendance/', views.mark_attendance, name='mark_attendance'),
    path('workforce/', views.workforce, name='workforce'),

    # task
    path('task-assignments/', views.task_assignments, name='task_assignments'),
    path('assign-task/', views.assign_task, name='assign_task'),
]
