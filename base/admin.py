from django.contrib import admin
from .models import Room, Topic ,Message,Profile
import django.apps





admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(Profile)

# models = django.apps.apps.get_models()
# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass

# admin.site.unregister(django.contrib.sessions.models.Session)