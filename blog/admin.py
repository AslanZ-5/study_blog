from django.contrib import admin
from .models import Post, Comment
from mptt.admin import MPTTModelAdmin
admin.site.register(Post)
admin.site.register(Comment, MPTTModelAdmin)
