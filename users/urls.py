from django.urls import path
from django.contrib.auth import views as auth_views
from .views  import (
    login_page,
    logout_user,
    register_page,
    userProfile,
    editUser,
     
                        )

app_name = 'users'

urlpatterns = [
    path('login/',login_page,name='login'),
    path('logout/',logout_user,name='logout'),
    path('register/',register_page,name='register'),
    path('profile/<str:pk>',userProfile,name='user-profile'),
    path('edit-user/<int:pk>/',editUser, name='edit_user' ),
    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(template_name='change-password.html'), name='change_password'
    ),


]