from django.shortcuts import render, redirect
from django import views
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.

class LoginView(views.View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        pwd = request.POST.get('password')
        is_check = request.POST.get('is_check', False)
        if len(pwd) < 8:
            return render(request, 'login.html', {'error_msg': '密码长度应不小于8位'})
        # print(auth.get_user_model())
        user_obj = auth.authenticate(request, email=email, password=pwd)
        if user_obj:
            auth.login(request, user_obj)
            if is_check:
                request.session.set_expiry(7*24*60*60)
            else:
                request.session.set_expiry(0)
            return redirect('/index/')
        else:
            return render(request, 'login.html', {'error_msg': '邮箱或密码错误'})


@login_required
def index(request):
    return HttpResponse('index')

def home(request):
    return redirect('home')