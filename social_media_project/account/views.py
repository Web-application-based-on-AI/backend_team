from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from django.shortcuts import render, get_object_or_404 , redirect
from django.contrib.auth.models import User , auth
from django.contrib.auth import authenticate
from .forms import SignupForm , LoginForm
from .models import User
from .decorators import user_is_loggedin
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.

@user_is_loggedin
def login_view(request):
    context = {
        'title' : 'Login'
    }
    if request.POST:
        form = LoginForm(request.POST)
        print("5")
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(email = email, password = password)
            auth.login(request,user)
            return redirect ('posts:home_page')
        else:
            context ['login_form'] = form
    else:
        form = LoginForm()
        context ['login_form'] = form
    return render (request,'account/login_form.html',context)


@user_is_loggedin
def signup_view(request):
    context = {
        'title' : 'sign up'
    }
    if request.POST:
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = auth.authenticate(username = email, password = password)
            auth.login(request,user)
            return redirect ('posts:home_page')
        else:
            context ['signup_form'] = form
    else:
        form = SignupForm()
        context ['signup_form'] = form
    return render (request,'account/signup_form.html',context)



def logout(request):
    auth.logout(request)
    return redirect('/')