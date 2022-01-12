from os import name
from django.urls import path,reverse_lazy
from django.contrib.auth import views as auth_views
from .views  import (
    login_page,
    logout_user,
    register_page,
    userProfile,
    editUser,
    password_success,
    PasswordsChangeView
     
                        )

app_name = 'users'

urlpatterns = [
    path('login/',login_page,name='login'),
    path('logout/',logout_user,name='logout'),
    path('register/',register_page,name='register'),
    path('profile/<str:pk>',userProfile,name='user-profile'),
    path('edit-user/<int:pk>/',editUser, name='edit_user' ),
    path('change-password/',PasswordsChangeView.as_view(), name='change_password'),
    path('password/success/',password_success,name='password_success'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html',
                                                                            email_template_name = 'password_reset_confirm.html'),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html',),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),






]