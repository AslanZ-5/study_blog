from django.urls import path

from . import api_views

urlpatterns = [
    path('',api_views.getRoutes),
    path('rooms/',api_views.getRooms),
    path('rooms/<str:pk>/',api_views.getRoom),
    ]