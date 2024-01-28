from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns =[
    path('', views.blogs_view, name='index'),
    path('<int:pid>', views.blogs_single, name='single'),
    path('category/<str:cat_name>', views.blogs_view, name='category'),
]