from profiles.models import Profiles
from django import template

register = template.Library() 

@register.simple_tag
def get_profile_informations(request_user):
    return Profiles.get_profile(request_user)
    
    