import uuid

from django.core.validators import MaxLengthValidator
from django.db import models
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse

User = get_user_model()
# Create your models here.
class Post(models.Model):
    idposts     = models.AutoField(primary_key=True)
    user_key    = models.ForeignKey(User,default = None ,on_delete=models.SET_NULL,null=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    content     = models.TextField(validators=[MaxLengthValidator(200)],blank=True)
    post_type   = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'posts'
        
    def __str__(self):
        return self.content
    
