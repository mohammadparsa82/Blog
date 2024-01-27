from django import template
from blogs.models import Post

register = template.Library()

@register.inclusion_tag('blogs/blog-latestposts.html')
def latestposts(arg=3):
    posts = Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts':posts}