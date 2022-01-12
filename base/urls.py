from django.urls import path
from .views import ( home,
                    room,
                    create_room,
                    update_room,
                    delete_room,
                    delete_message,
                    topics_view,
                    activities_view
                    )

app_name = 'base'

urlpatterns = [
    path('',home, name='home'),
    path('room/<str:pk>/',room, name='room'),
    path('create-room/',create_room, name='create_room' ),
    path('update-room/<int:pk>/',update_room, name='update_room' ),
    path('delete-room/<int:pk>/',delete_room, name='delete_room' ),
    path('delete-message/<int:pk>/',delete_message, name='delete_message' ),
    path('topics',topics_view,name='topics'),
    path('activities',activities_view,name='activities')

]