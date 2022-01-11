from django.urls import path
from .views import (
    HomeListView,
    PostDetailView,
    AddPostView,
    UpdatePostView,
    DeletePostView
)

app_name = 'blog'
urlpatterns = [
    path('',HomeListView.as_view(),name='home'),
    path('post/<str:slug>/',PostDetailView.as_view(),name='post_detail'),
    path('add-post/',AddPostView.as_view(),name='post_add'),
    path('update-post/<str:slug>/',UpdatePostView.as_view(),name='post_update'),
    path('delete-post/<str:slug>/',DeletePostView.as_view(),name='post_delete'),

]