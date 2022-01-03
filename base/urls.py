from django.urls import path
from .views import home,room

app_name = 'base'

urlpatterns = [
    path('',home, name='home'),
    path('room/<str:pk>/',room, name='room')
]