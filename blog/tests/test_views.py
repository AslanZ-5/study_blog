from cgitb import reset
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from blog.models import Post
from blog.views import DeleteView,HomeListView,AddPostView
from django.urls import reverse
from blog.forms import CommentForm

class PostTestCase(TestCase):
    
    def setUp(self):
        self.factory = RequestFactory()
        self.user_a = User.objects.create_user('user1','test12345')
        self.user_b = User.objects.create_user('user2','test12345')
        self.post_1 = Post.objects.create(title='hello',body='dddd',author=self.user_a)

    def test_users_count(self):
        quantity = User.objects.all().count()
        self.assertEqual(quantity,2)


    def test_valid_request(self):
        self.client.login(username=self.user_b.username,password='test12345')
        
        response = self.client.post('/add-post/',{'title':'this is a valid test','body':'this is test'})
       
        self.assertEqual(response.status_code,302)
        
    def test_details(self):
        response = self.client.get(f'/post/{self.post_1.title_tag}/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.context['post'].title,'hello')

    def test_details_create_comment(self):
        data = {'post':self.post_1,'content':'helllow','writer':self.user_a}
        form = CommentForm(data=data)
        self.client.login(username='user1', password='test12345')

        # self.assertEqual(response.status_code,200)
        # self.assertEqual(response.context['post'].title,'hello')
        self.assertTrue(form.is_valid())
    def test_home_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(len(response.context['object_list']),1)
    def test_home_view_query_search(self):
        response = self.client.get('/?q=hello')
        self.assertEqual(response.status_code,200)
        self.assertEqual(len(response.context['object_list']),1)
        self.assertEqual(response.context['object_list'][0].title,'hello')
    
    def test_add_post_view(self):
        self.client.login(username='user1', password='test12345')
        response = self.client.get(reverse('blog:post_update',args=[self.post_1.title_tag]))
        self.assertTrue(response.context['update'])
    
    # def test_add_likes(self):
    #     self.client.login(username='user1', password='test12345')
        


#                 py manage.py test blog.tests.view_tests