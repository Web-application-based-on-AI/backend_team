from django.db import models
from django.contrib.auth import get_user_model
from posts.models import Post

AccountUser = get_user_model()
# Create your models here.

class Comment(models.Model):
    idcomment       = models.AutoField(primary_key=True)
    posts_idposts   = models.ForeignKey(Post, on_delete=models.CASCADE , db_column='posts_idposts')
    comment_text    = models.CharField(max_length=150)
    created_at      = models.DateTimeField(auto_now_add=True)
    account_user    = models.ForeignKey(AccountUser, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'comments'

    # def get_comments_count(self):
    #     return Comment.objects.filter(Comment__posts_idposts=self.posts_idposts).count()
