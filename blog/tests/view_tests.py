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