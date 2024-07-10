from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('master/', views.master, name='master'),
    path('users/', views.users, name='users'),
    path('blogs/', views.blogs, name='blogs'),
    path('comments/', views.comments, name='comments'),
    path('categories/', views.categories, name='categories'),
    path('blog/<int:post_id>/', views.blog_details, name='blog_details'),
]
