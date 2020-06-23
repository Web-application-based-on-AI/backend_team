from django.shortcuts import render, get_object_or_404 , redirect

def user_is_loggedin(function , rediret_url = '/'):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(rediret_url)
        else:
            return function(request, *args, **kwargs)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
