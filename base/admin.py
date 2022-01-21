from django.contrib import admin
from .models import Room, Topic ,Message,Profile
import django.apps

class BaseAdminArea(admin.AdminSite):
    site_header = 'Base Admin Area'

base_site = BaseAdminArea(name='Base_arae')
base_site.register(Room)
base_site.register(Topic)
base_site.register(Message)
base_site.register(Profile)



models = django.apps.apps.get_models()
for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass

admin.site.unregister(django.contrib.sessions.models.Session)