from django.urls import path
from .views import (
    HomeListView,
    PostDetailView,
)

app_name = 'blog'
urlpatterns = [
    path('',HomeListView.as_view(),name='home'),
    path('post/<str:slug>/',PostDetailView.as_view(),name='post_detail'),
]