from django import template
from ..models import Post
from taggit.models import Tag
# Markdown is a text-to-HTML conversion tool
from django.utils.safestring import mark_safe
import markdown



register = template.Library()

@register.simple_tag
def total_posts():
    return Post.objects.count()

@register.inclusion_tag('blog/post/most_liked_posts.html')
def most_liked_posts(num=5):
    posts = Post.objects.all()[:num]
    return {'posts': posts}


# return all tags or a given number of tags
@register.inclusion_tag('blog/post/tags_list.html')
def tags_list(num=None):
    if num:
        tags_list = Tag.objects.all()
    else:
        tags_list = Tag.objects.all()[:num]

    return {'tags_list': tags_list}


@register.filter
def cut(value, arg):
    return value.replace(arg, ' ')

# register markdown filter
@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))


