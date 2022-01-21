from atexit import register
import imp
from django.contrib import admin
from .models import Post, Comment
from mptt.admin import MPTTModelAdmin
from django import forms

class PostForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(PostForm,self).__init__(*args,**kwargs)
        self.fields['title'].help_text = 'New Help Text'
        self.fields['title_tag'].help_text = '(title whose spaces replaced by hypen)-(post id)-(author id)  '

    class Meta:
        model = Post
        fields = '__all__'
    

TEXT = 'Some text for section one '
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    
    form = PostForm
    fieldsets = (
        ('Section 1',{
            'fields':('title','author'),
            'description': '%s' % TEXT,
        }),
        ('Section 2',{
            'fields':('title_tag',),
            'classes':('collapse',),
        }),
    )
    
   

     
admin.site.register(Comment, MPTTModelAdmin)