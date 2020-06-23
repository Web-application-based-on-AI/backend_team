from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager ,PermissionsMixin
from django.core.exceptions import ValidationError

GENDER_CHOICES = [
  ('Male', 'Male'),
  ('Female', 'Female'),
]

class UserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None, is_active=True, is_staff=False, is_superuser=False):
        # if not email:
        #     raise ValueError("Users must have an email address")
        # if not password:
        #     raise ValueError("Users must have a password")
        # if not full_name:
        #     raise ValueError("Users must have a name")

        user_obj = self.model(
            email = self.normalize_email(email),
            full_name = full_name
        )
        user_obj.set_password(password) # change user password
        user_obj.is_staff = is_staff
        user_obj.is_superuser = is_superuser
        user_obj.is_active = is_active
        try:
            user_obj.full_clean()
        except ValidationError as e:
            return e
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email,full_name=None, password=None):
        user = self.create_user(
                email,
                full_name = full_name,
                password = password,
                is_staff = True
        )
        return user

    def create_superuser(self, email, full_name=None, password=None):
        user = self.create_user(
                email,
                full_name = full_name,
                password = password,
                is_staff = True,
                is_superuser = True
        )
        return user 

# Create your models here.
class User (AbstractBaseUser):
    email               = models.EmailField(max_length=255, unique=True)
    is_active           = models.BooleanField(default=True)     # can login 
    is_staff            = models.BooleanField(default=False)    # staff user non superuser
    is_superuser        = models.BooleanField(default=False)
    date_created        = models.DateTimeField(auto_now_add=True)
    image               = models.ImageField(upload_to='profiles_images/',blank=True, null=True,default='images/avatar.png')
    full_name           = models.CharField(max_length=30)
    

    USERNAME_FIELD = 'email' #username for login
    REQUIRED_FIELDS = ['full_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return True
    
    class Meta:
        managed = False
        db_table = 'account_user'

    def save(self, *args, **kwargs):
            if not self.image:
                self.image = User._meta.get_field('image').get_default()
            super(User, self).save(*args, **kwargs)