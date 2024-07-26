from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def welcome(request):
    context={

    }
    return render(request,'core/app/welcome.html',context)