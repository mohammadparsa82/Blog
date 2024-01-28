from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns =[
    path('', views.blogs_view, name='index'),
    path('<int:pid>', views.blogs_single, name='single'),
    path('category/<str:cat_name>', views.blogs_view, name='category'),
    path('author/<str:author_username>', views.blogs_view, name='author'),
    path('search/',views.blogs_search,name='search'),
]