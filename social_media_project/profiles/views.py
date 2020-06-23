from .models import Profiles
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CreateProfileForm,UpdateMailNameForm
from django.contrib.auth.forms import PasswordChangeForm

User = get_user_model()

# Create your views here.

def profile_view(request):
    context = {
        'title' : request.user.full_name
    }
    profile_obj = Profiles.get_profile(request.user)
    if not profile_obj:
        return redirect('profiles:create_profile')
    
    context['profile_obj'] = profile_obj
    return render(request,'profiles/profile.html',context)

def profile_others_view(request,user_id):
    profile_obj = get_object_or_404(Profiles,account_user = user_id)
    context = {
        'title' : profile_obj.account_user.full_name
    }
    context['profile_obj'] = profile_obj
    return render(request,'profiles/profile.html',context)

def create_profile_view(request):
    context = {
        'title' : 'Create Profile'
    }
    if request.POST:
        form = CreateProfileForm(request.POST , request.FILES or None)
        if form.is_valid():
            profile_obj = form.save(commit=False)
            profile_obj.account_user = request.user
            profile_obj.save()
            return redirect('profiles:profile')
        else:
            context['create_profile_form'] = form
            return render(request,'profiles/create_profile.html',context)
    else:
        profile_obj = Profiles.get_profile(request.user)
        if profile_obj:
            return redirect('profiles:profile')
        form = CreateProfileForm()
        context['create_profile_form'] = form
        return render(request,'profiles/create_profile.html',context)

def edit_mail_name_view(request):
    context = {
        'title' : 'Edit profile'
    }
    if request.POST:
        form = UpdateMailNameForm(request.POST, files = request.FILES or None ,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect ('profiles:profile')
        else:
            return edit_profile_view(request,mail_name_form = form)
    return redirect('profiles:edit')

def edit_password_view(request):
    context = {
        'title' : 'Edit profile'
    }
    if request.POST:
        form = PasswordChangeForm(user=request.user , data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user) #user doesn't have to sign in again
            return redirect ('profiles:profile')
        else:
            return edit_profile_view(request,password_form=form)
    else:
        return redirect('profiles:edit')

def edit_info_view(request):
    context = {
        'title' : 'Edit profile'
    }
    profile_obj = Profiles.get_profile(request.user)
    if request.POST:
        form = CreateProfileForm(request.POST , files = request.FILES or None ,instance=profile_obj )
        if form.is_valid():
            form.save()
            return redirect ('profiles:profile')
        else:
            return edit_profile_view(request,info_form=form)
    return redirect('profiles:edit')

def edit_profile_view(request,password_form = None, info_form = None,mail_name_form = None):
    context = {
        'title' : 'Edit Account Data'
    }
    if not mail_name_form:
        mail_name_form = UpdateMailNameForm(instance = request.user)
    if not password_form:
        password_form = PasswordChangeForm(user = request.user)
    if not info_form:
        profile_obj = Profiles.get_profile(request.user)
        info_form = CreateProfileForm(instance=profile_obj)
    context['edit_mail_name_form'] = mail_name_form
    context['edit_password_form'] = password_form
    context['edit_info_form'] = info_form
    return render(request,'profiles/edit_profile.html',context)
