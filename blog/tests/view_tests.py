from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post

class PostTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('user1','test12345')
        self.user_b = User.objects.create_user('user2','test12345')

    def test_users_count(self):
        quantity = User.objects.all().count()
        self.assertEqual(quantity,2)


    def test_valid_request(self):
        self.client.login(username=self.user_b.username,password='test12345')
        response = self.client.post('/add-post/',{'title':'this is a valid test','body':'this is test'})
        self.assertEqual(response.status_code,302)
        


    def test_not_login_request(self):
        response = self.client.get('/add-post/',follow=True)
        print('aaa',response.resolver_match)
       
        # self.assertEqual(response.status_code,302)

    def test_list_view_response(self):
        pass
        # response = self.client.get('/')
        # print(response.context.get('object_list'))
    

#                 py manage.py test blog.tests.view_tests