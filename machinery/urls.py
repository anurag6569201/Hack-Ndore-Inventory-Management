from django.urls import path
from machinery import views

app_name='machinery'

urlpatterns=[
    path('',views.machinery,name='machinery'),
]