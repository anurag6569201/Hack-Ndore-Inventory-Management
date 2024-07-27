from django.urls import path
from maintain import views

app_name='maintain'

urlpatterns=[
    path('',views.maintain,name='maintain'),
]