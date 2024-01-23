from django.shortcuts import render
from blogs.models import Post


def blogs_view(request):
    posts = Post.objects.filter(status = 1)
    context = {'posts': posts}
    return render(request, 'blogs/blog-home.html', context)

def blogs_single(request):
    return render(request,'blogs/blog-single.html')
