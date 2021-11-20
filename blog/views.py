from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from .models import Post

def home(request):
    saving_posts = Post.objects.filter(category=1)
    investing_posts = Post.objects.filter(category=2)
    mindest_posts = Post.objects.filter(category=3)
    motivation_posts = Post.objects.filter(category=4)
    context = {
        'posts': Post.objects.all(),
        'title': 'Basic Million',
        'saving_posts': saving_posts,
        'investing_posts': investing_posts,
        'mindest_posts': mindest_posts,
        'motivation_posts': motivation_posts,
    }
    return render(request, 'blog/home.html', context)

# Category number key - 1: Saving, 2: Investing, 3: Mindest, 4: Motivation
def saving(request):
    saving_posts = Post.objects.filter(category=1)
    context = {
        'posts': Post.objects.all(),
        'title': 'Saving',
        'saving_posts': saving_posts,
    }
    return render(request, 'blog/saving.html', context)

def investing(request):
    investing_posts = Post.objects.filter(category=2)
    context = {
        'posts': Post.objects.all(),
        'title': 'Investing',
        'investing_posts': investing_posts,
    }
    return render(request, 'blog/investing.html', context)

def mindset(request):
    mindest_posts = Post.objects.filter(category=3)
    context = {
        'posts': Post.objects.all(),
        'title': 'Mindset',
        'mindest_posts': mindest_posts,
    }
    return render(request, 'blog/mindset.html', context)

def motivation(request):
    motivation_posts = Post.objects.filter(category=4)
    context = {
        'posts': Post.objects.all(),
        'title': 'Motivation',
        'motivation_posts': motivation_posts,
    }
    return render(request, 'blog/motivation.html', context)

def about(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'About',
    }
    return render(request, 'blog/about.html', context)

def postcard(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Postcard',
    }
    return render(request, 'blog/postcard.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted'] # Reorder blogs from oldest first to newest first
    paginate_by = 5 # Limits number of blogs per page

class PostDetailView(DetailView):
    model = Post
