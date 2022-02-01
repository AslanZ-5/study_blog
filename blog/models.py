from re import T
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from mptt.models import MPTTModel,TreeForeignKey



class Post(models.Model):
    title = models.CharField(max_length=220, help_text='This  title is required')
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title_tag = models.CharField(max_length=220,unique=True,blank=True,help_text='automatically maded')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # category = 
    # header_image = 
    likes = models.ManyToManyField(User,related_name='blog_post')
    body = models.TextField(blank=True,null=True)

    def __str__(self):
        return f'Post "{self.title}"'
    
    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug':self.title_tag})
    
    def save(self,*args,**kwargs):
        try:
            a = Post.objects.all().last().id
        except:
            a = 0
        self.title_tag = f"{self.title.replace(' ', '-')}-{a+1}-{self.author.id}"
        super().save(*args,**kwargs)
    class Meta:
        ordering = ['-created']
        
class Comment(MPTTModel):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    parent = TreeForeignKey('self',on_delete=models.CASCADE, null=True,blank=True,related_name='children')
    writer = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ['created']
        
    def __str__(self):
        return f'Comment "{self.content[:50]}" by {self.writer.username}'

