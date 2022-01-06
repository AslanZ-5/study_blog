from django.urls import path
from .views import (editUser, home,
                    room,
                    create_room,
                    update_room,
                    delete_room,
                    login_page,
                    logout_user,
                    register_page,
                    delete_message,
                    userProfile,
                    editUser,
                    )

app_name = 'base'

urlpatterns = [
    path('login/',login_page,name='login'),
    path('logout/',logout_user,name='logout'),
    path('register/',register_page,name='register'),
    path('',home, name='home'),
    path('profile/<str:pk>',userProfile,name='user-profile'),
    path('room/<str:pk>/',room, name='room'),
    path('create-room/',create_room, name='create_room' ),
    path('update-room/<int:pk>/',update_room, name='update_room' ),
    path('delete-room/<int:pk>/',delete_room, name='delete_room' ),
    path('delete-message/<int:pk>/',delete_message, name='delete_message' ),
    path('edit-user/<int:pk>/',editUser, name='edit_user' ),

]