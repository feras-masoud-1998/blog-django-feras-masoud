from django.db.models import fields
from .models import Comment, Post
from django import forms

class NewComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class PostCreateForm(forms.ModelForm):
    title = forms.CharField(label='عنوان التدوينة')
    content = forms.CharField(label='نص التدوينة', widget=forms.Textarea)
    class Meta:
        model = Post
        fields = ['title', 'content']
