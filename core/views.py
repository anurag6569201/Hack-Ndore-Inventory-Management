from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

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
    context={

    }
    return render(request,'core/app/user_index.html',context)