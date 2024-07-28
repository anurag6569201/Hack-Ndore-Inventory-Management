from django.urls import path
from maintain import views

app_name='maintain'

urlpatterns=[
    path('',views.maintain,name='maintain'),
    path('remainder',views.remainder,name='remainder'),
    path('repair',views.view_repair_activities,name='repair'),
]