from django.urls import path
from .views import home,room,create_room,update_room

app_name = 'base'

urlpatterns = [
    path('',home, name='home'),
    path('room/<str:pk>/',room, name='room'),
    path('create-room/',create_room, name='create_room' ),
    path('update-room/<int:pk>/',update_room, name='update_room' ),
]