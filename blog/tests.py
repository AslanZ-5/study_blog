from django.test import TestCase
from .models import Post 
from django.contrib.auth.models import User


class PostTestCase(TestCase):
    def setUp(self):
        for i in range(1,7+1):
            a = User.objects.create_user(username=f'user{i}',password='test123456')
            Post.objects.create(title=f'post has been created by {a.username}',author=a,body='random text for post {i}')
    def test_user_password(self):
        checked = User.objects.all().first().check_password('test123456')
        self.assertTrue(checked)
            
    def test_count_users_and_posts(self):
        users_quantity = User.objects.all().count() 
        posts_quantity = Post.objects.all().count()
        self.assertTrue(users_quantity,7) 
        self.assertTrue(posts_quantity,7) 


        
#py manage.py test blog