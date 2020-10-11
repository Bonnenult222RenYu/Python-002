from django.shortcuts import render, redirect
from django import views
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .form import LoginForm
# Create your views here.

class LoginView(views.View):
    def get(self, request):
        form_obj = LoginForm() 
        return render(request, 'login.html', {'form': form_obj})

    def post(self, request):
        form_obj = LoginForm(request.POST) 
        if form_obj.is_valid():
            user_obj = auth.authenticate(request, **form_obj.cleaned_data)
            is_check = request.POST.get('is_check', None)
            if user_obj:
                auth.login(request, user_obj)
                if is_check:
                    request.session.set_expiry(7*24*60*60)
                else:
                    request.session.set_expiry(0)
                return redirect('/index/')
            return render(request, 'login.html', {'error_msg': '邮箱或密码错误', 'form': form_obj})
        else:
            return render(request, 'login.html', {'form': form_obj})


@login_required
def index(request):
    return HttpResponse('index')

def home(request):
    return redirect('/index')