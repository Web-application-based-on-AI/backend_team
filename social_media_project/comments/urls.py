from django.urls import path

from . import views

app_name = 'comments'
urlpatterns = [
    # comment/
    path('add/<int:post_id>/', views.comment_add_view, name='add_comment'),
    path('delete/<int:comment_id>/', views.comment_delete_view, name='delete_comment'),
    path('log/', views.comment_log_view, name='comment_log'),
    
]
