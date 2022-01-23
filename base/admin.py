from django.contrib import admin
from .models import Room, Topic ,Message,Profile
import django.apps
from django.contrib.admin import SimpleListFilter



class EmailFilter(SimpleListFilter):
    title = ('Email Filter',)
    parameter_name = 'user_email'
    def lookups(self,request,model_admin):
        return (
            ('has_email','has_email'),
            ('no_email','no_email')
        )
    def queryset(self,request,queryset):
        if not self.value():
            return queryset
        if self.value().lower() == 'has_email':
            return queryset.exclude(user__email='')
        if self.value().lower() == 'no_email':
            return queryset.filter(user__email='')
class Filter(admin.ModelAdmin):
    list_display = ('id','email','user','bio',)
    list_filter = ('role',EmailFilter)


class BaseAdminArea(admin.AdminSite):
    site_header = 'Base Admin Area'
    login_template = 'admin/admin.html'

base_site = BaseAdminArea(name='BaseAdmin')


class BaseAdmin(admin.ModelAdmin):
    list_display = ('name','id','topic','host')
    list_filter = ('topic','host')

base_site.register(Room,BaseAdmin)
base_site.register(Topic)
base_site.register(Message)
base_site.register(Profile)




admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(Profile,Filter)

# models = django.apps.apps.get_models()
# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass

# admin.site.unregister(django.contrib.sessions.models.Session)