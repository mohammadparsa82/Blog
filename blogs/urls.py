from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns =[
    path('', views.blogs_view, name='index'),
    path('single/', views.blogs_single, name='single'),
]