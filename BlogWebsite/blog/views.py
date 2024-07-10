
from django.shortcuts import render
from .models import User, Post, Comment, Category


def main(request):
    return render(request, 'main.html')

def master(request):
    return render(request, 'master.html')

def users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})

def blogs(request):
    posts = Post.objects.all()
    return render(request, 'blogs.html', {'posts': posts})

def comments(request):
    comments = Comment.objects.all()
    return render(request, 'comments.html', {'comments': comments})

def categories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})

def blog_details(request, post_id):
    post = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post=post)
    return render(request, 'blogdetails.html', {'post': post, 'comments': comments})
