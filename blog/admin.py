from django.contrib import admin
from .models import Post, Comment
from mptt.admin import MPTTModelAdmin


class BlogAdminArea(admin.AdminSite):
    site_header = 'Blog ____'


blog_site = BlogAdminArea(name='BlogAdmin__')
blog_site.register(Post)


admin.site.register(Post)
admin.site.register(Comment, MPTTModelAdmin)