from django.contrib import admin
from .models import Room, Topic ,Message,Profile
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(Profile)

class BaseAdminArea(admin.AdminSite):
    site_header = 'Base Admin Area'

base_site = BaseAdminArea(name='Base_arae')
base_site.register(Room)
base_site.register(Topic)
base_site.register(Message)
base_site.register(Profile)
