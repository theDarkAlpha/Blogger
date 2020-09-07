from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.

class HomePage(ListView):
    model = Post
    template_name = 'home.html'

class BlogPage(DetailView):
    model = Post
    template_name = 'Detail_Blog.html'