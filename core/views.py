from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from core.forms import ProblemForm
from django.views.decorators.csrf import csrf_exempt
import json
from core.LLM_Model.test import get_response
from langchain.prompts import ChatPromptTemplate

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