from django.urls import path

from . import views

app_name = 'account'
urlpatterns = [
    # ex: /account/login
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout, name='logout'),
    # # ex: /polls/5/
    # path('regestration/', views.regestration, name='regestration'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]