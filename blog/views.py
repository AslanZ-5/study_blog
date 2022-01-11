from django.db import models
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post

class HomeListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post
    slug_field = 'title_tag'




