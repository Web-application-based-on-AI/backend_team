from django import forms
from .models import Profiles
from django.contrib.auth import get_user_model

# GENDER_CHOICES = [
#   ('Male', 'Male'),
#   ('Female', 'Female')
# ]
User = get_user_model()

class CreateProfileForm (forms.ModelForm):
    # gender = forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect)
    class Meta:
        model = Profiles
        fields = ['birthdate', 'gender', 'career', 'country']

class UpdateMailNameForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['email','full_name','image']