from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    # ex: /
    
    path('', views.home_page_view, name='home_page'),
    path('staff_page', views.staff_page_view, name='staff_page'),
    path('<int:user_id>/posts/', views.user_posts_view, name='user_posts'),
    path('<int:post_id>/details/', views.post_details_view, name='post_details'),
    path('<int:post_id>/delete/', views.post_delete_view, name='post_delete'),
    path('create_post', views.create_post_view, name='create_post'),
    path('show_error', views.show_error_view, name='show_error'),

    # ex: /polls/5/
    # path('regestration/', views.regestration, name='regestration'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]
