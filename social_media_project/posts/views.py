from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import reverse 
from django.http import request
from . import models
from comments.forms import CommentForm
from comments.models import Comment
import pickle
import numpy as np


site_type = "religion"
loaded_model = pickle.load(open('ai_model/naive_bayes_97.sav', 'rb'))
count_vect = pickle.load(open('ai_model/count_vect97', 'rb'))
post_types = {
    0:'Politic',
    1:'ads',
    2:'economic',
    3:'food',
    4:'health',
    5:'adult',
    6:'religion',
    7:'sports',
    8:'teching',
    9:'tv',
}

# Create your views here.
# @login_required(login_url='/account/login/')
def home_page_view(request):
    posts_objects = models.Post.objects.filter(post_type = site_type).order_by('-created_at')
    template_name = 'posts/home_page.html'
    comments = Comment.objects.all()
    for post in posts_objects:
        post.comment_count = comments.filter(posts_idposts=post.idposts).count()
    context = {
        'posts': posts_objects,
    }
    return render(request, template_name, context)

def user_posts_view(request,user_id):
    posts_objects = models.Post.objects.filter(post_type = site_type,user_key=user_id).order_by('-created_at')
    template_name = 'posts/user_posts.html'
    comments = Comment.objects.all()
    for post in posts_objects:
        post.comment_count = comments.filter(posts_idposts=post.idposts).count()
    context = {
        'posts': posts_objects,
    }
    return render(request, template_name, context)

@staff_member_required
def staff_page_view(request):
    template_name = 'posts/staff_page.html'
    context ={
        'title': 'Staff page',
    }
    if request.POST:
        date = request.POST['from_date']
        posts_objects = models.Post.objects.filter(created_at__date__gt= date)
        data = ""
        for post in posts_objects:
            data+= "[{0},{1}]\n".format(post.post_type,post.content) 
        response = HttpResponse(data,content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename="trainig_data.txt"'
        return response
    else:
        return render(request,template_name,context)
        


def post_details_view(request,post_id,comment_form = None):
    template_name = 'posts/details.html'
    post = get_object_or_404(models.Post,pk = post_id)
    if post.post_type != site_type:
        raise Http404("")
    comments = Comment.objects.filter(posts_idposts=post_id).order_by('-created_at')
    post.comment_count = comments.count()
    if not comment_form:
        comment_form = CommentForm()
    context = {
        'post': post,
        'comments' : comments,
        'comment_form' : comment_form,
    }
    return render(request, template_name, context)

def create_post_view(request):
    if request.method == 'POST':
        post_content = request.POST['post_content']
        if len(post_content) == 0:
            return redirect('showerror')
        else:
            new = models.Post()
            new.content = post_content
            new.user_key = request.user
            new.post_type = get_post_type(post_content)
            new.save()
            if new.post_type == site_type:
                return redirect('posts:home_page')
            else:
                return render(request, 'posts/recommend.html', {'kind':new.post_type})
    else:
        return redirect('posts:home_page')


def show_error_view(request):
    template_name = 'error.html'
    return render(request, template_name, {})


def post_delete_view(request,post_id):
    post_obj = get_object_or_404(models.Post,pk=post_id)
    if request.user != post_obj.user_key:
        raise Http404("")
    post_obj.delete()
    return redirect('posts:home_page')

def get_post_type(content):
    fu = np.array(content, dtype=object)
    fu = fu.astype(str)
    z = count_vect.transform(fu.ravel())
    result = loaded_model.predict(z)[0]
    print(post_types[7])
    return post_types[result]
    