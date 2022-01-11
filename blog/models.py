from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=220)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title_tag = models.CharField(max_length=220,unique=True,blank=True)
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
        a = Post.objects.all().last().id
        self.title_tag = f"{self.title.replace(' ', '-')}-{a+1}-{self.author.id}"
        super().save(*args,**kwargs)



