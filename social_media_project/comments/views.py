from django.http import Http404
from .models import Comment
from .forms import CommentForm
from posts.models import Post
from django.shortcuts import render, get_object_or_404, redirect
from posts.views import post_details_view

def comment_add_view(request,post_id):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_obj = form.save(commit=False)
            comment_obj.posts_idposts = get_object_or_404(Post,pk=post_id)
            comment_obj.account_user = request.user
            comment_obj.save()
            return redirect('posts:post_details',post_id= post_id)
        else:
            return post_details_view(request,post_id,form)
    else:
        return redirect('posts:home_page')

def comment_delete_view(request,comment_id):
    comment_obj = get_object_or_404(Comment,pk=comment_id)
    post_id = comment_obj.posts_idposts.idposts
    if request.user != comment_obj.account_user:
        raise Http404("")
    comment_obj.delete()
    return redirect('posts:post_details',post_id = post_id)

def comment_log_view(request):
    comments = Comment.objects.filter(account_user=request.user).order_by('-created_at')
    context = {
    'title' : 'comments log'
    }
    context['comments'] = comments
    return render(request,'comments/comment_log.html',context)

