from django.shortcuts import render , get_object_or_404
from blogs.models import Post ,comment
from django.core.paginator import Paginator ,EmptyPage ,PageNotAnInteger
from blogs.forms import CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def blogs_view(request, **kwargs):
    posts = Post.objects.filter(status = 1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])

    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])
        
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tag__name__in=[kwargs['tag_name']])
    posts = Paginator(posts,3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
        
    context = {'posts': posts}
    return render(request, 'blogs/blog-home.html', context)

def blogs_single(request,pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your comment submited successfully')
        else:
            messages.add_message(request,messages.ERROR,'your comment didnt submited')
   
    posts = Post.objects.filter(status = 1)
    post = get_object_or_404(posts, id = pid)
    comments = comment.objects.filter(post=post.id,approved=True)
    form = CommentForm()
    context = {'post':post,'comments':comments, 'form':form}
    return render(request,'blogs/blog-single.html', context)


def blogs_search(request):
    posts = Post.objects.filter(status = 1)
    if request.method == 'GET':
        if s:= request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {'posts': posts}
    return render(request, 'blogs/blog-home.html', context)