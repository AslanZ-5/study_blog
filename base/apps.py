from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig



class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'
    def ready(self):
        import base.signals
