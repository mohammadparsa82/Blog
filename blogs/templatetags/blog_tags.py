from django import template
from blogs.models import Post , Category , comment

register = template.Library()

@register.inclusion_tag('blogs/blog-latestposts.html')
def latestposts(arg=3):
    posts = Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts':posts}

@register.inclusion_tag('blogs/blog-category.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {'categories':cat_dict}

@register.simple_tag(name='comments_count')
def function(pid):
    post = Post.objects.get(pk=pid)
    return comment.objects.filter(post=post.id,approved=True).count()
