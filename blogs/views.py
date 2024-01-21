from django.shortcuts import render

def blogs_view(request):
    return render(request, 'blogs/blog-home.html')

def blogs_single(request):
    return render(request,'blogs/blog-single.html')
