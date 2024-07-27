from core import views
from django.urls import path

app_name="core"

urlpatterns=[
    path("",views.check,name="check"),
    path("home/",views.welcome,name="welcome"),
    path("userhome/",views.user_index,name="user_index"),
]
