from django.db import models
from django.shortcuts import render,redirect
from django.urls.converters import SlugConverter
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy


class HomeListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post
    slug_field = 'title_tag'



class AddPostView(CreateView):
    model = Post
    fields = ['title','author','body']




class UpdatePostView(UpdateView):
    model = Post
    slug_field = 'title_tag'
    fields = ['title','author','body']


class DeletePostView(DeleteView):
    model = Post
    slug_field = 'title_tag'
    success_url = reverse_lazy('blog:home')


    
