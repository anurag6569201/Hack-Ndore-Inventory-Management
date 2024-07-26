from django.urls import path
from assets_manage import views

app_name='assets_manage'

urlpatterns=[
    path('',views.assets_manage,name='assets_manage'),
    path('vehicle/', views.vehicle_list, name='vehicle_list'),
    path('vehicle/<int:pk>/', views.vehicle_detail, name='vehicle_detail'),
    path('vehicle/add/', views.vehicle_add, name='vehicle_add'),
]