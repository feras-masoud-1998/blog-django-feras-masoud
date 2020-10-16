from ..models import Post, Comment
from django import template

register = template.Library()

@register.inclusion_tag('blog/latest_posts.html')
def latest_posts():
    context = {
        'l_posts': Post.objects.all()[0:5]
    }
    return context


@register.inclusion_tag('blog/latest_comment.html')
def latest_comments():
    context = {
        'l_comments': Comment.objects.filter(active=True)[:5]
    }
    return context
