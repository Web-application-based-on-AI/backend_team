from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

class SignupForm (UserCreationForm):
    class Meta:
        model = User
        fields = [ 'email' ,'password1','password2','full_name']
        labels = {
            'email': 'Email Address',
        }
        # fields = "__all__"

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['email','password']
        labels = {
            'email': 'Email Address',
        }
    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        print(authenticate(email = email, password = password))
        if not authenticate(email = email, password = password):
            raise forms.ValidationError("Invalid login")
            
