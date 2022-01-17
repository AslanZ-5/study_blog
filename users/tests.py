from django.test import TestCase
from django.urls import reverse

class BaseTest(TestCase):
    def setUp(self):
        self.register_url = reverse('users:register')
        self.user = {
            'username':'user1',
            'email':'user1@gmail.com',
            'first_name':'musa',
            'last_name':'dadien',
            'password1':'test12345',
            'password2':'test12345'
        }
        self.user_short_password = {
            'username':'user_short',
            'email':'user1@gmail.com',
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