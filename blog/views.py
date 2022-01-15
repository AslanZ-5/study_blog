from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect,get_list_or_404
from django.urls import reverse
from django.urls.converters import SlugConverter
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import Post,Comment
from django.views.generic.edit import FormMixin
from django.views.generic.detail import DetailView

from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .forms import CommentForm

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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['popular_posts'] = Post.objects.all().order_by('-likes')[:5]
        return context

class PostDetailView(FormMixin,DetailView):
    model = Post
    slug_field = 'title_tag'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('blog:post_detail',kwargs={'slug':self.object.title_tag})
    
    def get_context_data(self, *args,**kwargs):
        like_post = get_object_or_404(Post,title_tag=self.kwargs['slug'])
        context = super(PostDetailView,self).get_context_data(*args,**kwargs)
        liked = False
        if like_post.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['liked'] = liked
        context['form'] = CommentForm(initial={'post':self.object})
        return context

    def post(self,request,*args,**kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    def form_valid(self,form):
        form.instance.writer_id = self.request.user.id
        form.instance.post = self.get_object()

        form.save()
        return super().form_valid(form)


        



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


    
