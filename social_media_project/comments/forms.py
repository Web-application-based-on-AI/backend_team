from django import forms
from .models import Comment


class CommentForm (forms.ModelForm):
    comment_text = forms.CharField( widget=forms.Textarea )
    class Meta:
        model = Comment
        fields = ['comment_text']
