from atexit import register
import imp
from django.contrib import admin
from .models import Post, Comment
from mptt.admin import MPTTModelAdmin
from django import forms
from django_summernote.admin import SummernoteModelAdmin


class PostForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(PostForm,self).__init__(*args,**kwargs)
        self.fields['title'].help_text = 'New Help Text'
        self.fields['title_tag'].help_text = '(title whose spaces replaced by hypen)-(post id)-(author id)  '

    class Meta:
        model = Post
        fields = '__all__'

class SummerAdmin(SummernoteModelAdmin):
    summernote_fields = "__all__"  

TEXT = 'Some text for section one '
@admin.register(Post)
class PostAdmin(SummerAdmin,admin.ModelAdmin):
    form = PostForm
    readonly_fields = ('created','updated')
    fieldsets = (
        ('Section 1',{
            'fields':('title','author'),
            'description': '%s' % TEXT,
        }),
        ('Section 2',{
            'fields':('title_tag',),
            'classes':('collapse',),
        }),
        ('Section 3',{
            'fields':('likes',('created','updated')),
            
        }),
        ('Section 4',{
            'fields':('body',),
            
        }),
    )
    
   



admin.site.register(Comment, MPTTModelAdmin)