from django.urls import path
from .views import (home,
                    room,
                    create_room,
                    update_room,
                    delete_room,
                    login_page,
                    logout_user
                    )

app_name = 'base'

urlpatterns = [
    path('login/',login_page,name='login'),
    path('logout/',logout_user,name='logout'),
    path('',home, name='home'),
    path('room/<str:pk>/',room, name='room'),
    path('create-room/',create_room, name='create_room' ),
    path('update-room/<int:pk>/',update_room, name='update_room' ),
    path('delete-room/<int:pk>/',delete_room, name='delete_room' ),
]