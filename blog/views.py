from django.db import models
from django.db.models import query
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from django.urls.converters import SlugConverter
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404


def LikePost(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('blog:post_detail', args=[post.title_tag]))



class HomeListView(ListView):
    model = Post
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            obj_list = self.model.objects.filter(Q(title__icontains=query)|
                                                    Q(body__icontains=query)|
                                                    Q(author__username__icontains=query))
        else:
            obj_list = self.model.objects.all()
        return obj_list

class PostDetailView(DetailView):
    model = Post
    slug_field = 'title_tag'
    def get_context_data(self, *args,**kwargs):
        like_post = get_object_or_404(Post,title_tag=self.kwargs['slug'])
        context = super(PostDetailView,self).get_context_data(*args,**kwargs)
        liked = False
        if like_post.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['liked'] = liked
        return context

        



class AddPostView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)




class UpdatePostView(UpdateView):
    model = Post
    slug_field = 'title_tag'
    fields = ['title','body']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = True
        return context


class DeletePostView(DeleteView):
    model = Post
    slug_field = 'title_tag'
    success_url = reverse_lazy('blog:home')


    
