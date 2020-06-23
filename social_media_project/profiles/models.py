from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

GENDER_CHOICES = [
  ('Male', 'Male'),
  ('Female', 'Female')
]

# Create your models here.
class Profiles(models.Model):
    idprofiles = models.AutoField(primary_key=True)
    birthdate = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True, choices=GENDER_CHOICES)
    career = models.CharField(max_length=45, blank=True, null=True)
    country = models.CharField(max_length=45, blank=True, null=True)
    account_user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'profiles'
    
    def get_profile(use_id):
      try:
        profile_obj = Profiles.objects.get(account_user=use_id)
      except Profiles.DoesNotExist :
        return None
      return profile_obj