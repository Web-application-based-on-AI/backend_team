from django.urls import path

from . import views

app_name = 'profiles'
urlpatterns = [
    # ex : profile/
    path('', views.profile_view, name='profile'),
    path('<int:user_id>', views.profile_others_view, name='profile_others_view'),
    path('create',views.create_profile_view, name='create_profile'),
    path('edit',views.edit_profile_view, name='edit'),
    path('edit_mail_name',views.edit_mail_name_view, name='edit_mail_name'),
    path('edit_password',views.edit_password_view, name='edit_password'),
    path('edit_info',views.edit_info_view, name='edit_info'),
]