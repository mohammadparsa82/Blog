from django.shortcuts import render , get_object_or_404
from blogs.models import Post


def blogs_view(request, **kwargs):
    posts = Post.objects.filter(status = 1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])
    context = {'posts': posts}
    return render(request, 'blogs/blog-home.html', context)

def blogs_single(request,pid):
    posts = Post.objects.filter(status = 1)
    post = get_object_or_404(posts, id = pid)
    context = {'post':post}
    return render(request,'blogs/blog-single.html', context)


#This part is related to the category that we summarized in the view instead of using this code
#def blogs_category(request,cat_name):
    posts = Post.objects.filter(status = 1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts':posts}
    return render(request,'blogs/blog-home.html', context)