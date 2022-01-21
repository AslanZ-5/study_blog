from atexit import register
from django.contrib import admin
from .models import Post, Comment
from mptt.admin import MPTTModelAdmin


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


admin.site.register(Comment, MPTTModelAdmin)