from core import views
from django.urls import path

app_name="core"

urlpatterns=[
    path("",views.check,name="check"),
    path("home/",views.welcome,name="welcome"),
    path("userhome/",views.user_index,name="user_index"),
    path("success/",views.user_form_success,name="user_form_success"),
    path('send-message/', views.send_message, name='send_message'),
]
