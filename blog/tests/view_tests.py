from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from blog.models import Post
from blog.views import DeleteView,HomeListView

class PostTestCase(TestCase):
    
    def setUp(self):
        self.factory = RequestFactory()
        self.user_a = User.objects.create_user('user1','test12345')
        self.user_b = User.objects.create_user('user2','test12345')

    def test_users_count(self):
        quantity = User.objects.all().count()
        self.assertEqual(quantity,2)


    def test_valid_request(self):
        self.client.login(username=self.user_b.username,password='test12345')
      
        response = self.client.post('/add-post/',{'title':'this is a valid test','body':'this is test'})

        self.assertEqual(response.status_code,302)
        
    def test_details(self):
        a = Post.objects.create(title='hello',body='dddd',author=self.user_a)
        response = self.client.get(f'/post/{a.title_tag}/')
      
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.context['post'].title,'hello')
    

#                 py manage.py test blog.tests.view_tests