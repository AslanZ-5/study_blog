"""study_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from base.admin import base_site

urlpatterns = [
    path('admin/',admin.site.urls),
    path('base-admin/',base_site.urls),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('rooms/',include('base.urls')),
    path('',include('blog.urls')),
    path('summernote/',include('django_summernote.urls')),
    path('api/', include('base.api.api_urls')),
    path('users/',include('users.urls')),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html',),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),

]

if settings.DEBUG:
    urlpatterns +=  static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
admin.site.index_title = 'The Study Blog'
admin.site.site_header = 'The Study Blog Administrations'
admin.site.site_title = 'Sudy Blog Admin'