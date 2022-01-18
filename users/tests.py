from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from users import forms

class BaseTest(TestCase):
    def setUp(self):
        self.register_url = reverse('users:register')
        self.login_url = reverse('users:login')
        self.user = {
            'username':'user123',
            'email':'user11111py@gmail.com',
            'first_name':'musa',
            'last_name':'dadien',
            'password1':'test12345',
            'password2':'test12345'
        }
        self.user_short_password = {
            'username':'user_short',
            'email':'user_hort1@gmail.com',
            'first_name':'musa',
            'last_name':'dadien',
            'password1':'test',
            'password2':'test'
        }
        return super().setUp()
        
class RegisterTest(BaseTest):

    def test_can_view_correctly(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'login_register.html')

    def test_can_register_user(self):
        response = self.client.post(self.register_url,self.user,format='text/html')
        self.assertEqual(response.status_code,302)

    def test_cant_register_user(self):
        response = self.client.post(self.register_url,self.user_short_password,format='text/html')
        self.assertEqual(response.status_code,400)

class LoginTest(BaseTest):

    def test_can_access_page(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'login_register.html')


    def test_login_success(self):
        g = self.client.post(self.register_url,self.user,format='text/html')
        self.assertEqual(g.status_code,302)
        user = User.objects.filter(username=self.user['username']).first()
        user.is_active = True
        self.assertTrue(user.is_active)
        user.save()
        response = self.client.post(self.login_url,self.user,format='text/html')
       
        self.assertEqual(response.status_code,302)

    def test_cant_login(self):
        response = self.client.post(self.login_url,{'password':'test12345'},format='text/html')
        self.assertNotEqual(response.status_code,302)