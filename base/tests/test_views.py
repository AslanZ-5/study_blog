import imp
from urllib import response
from django.test import TestCase
from django.urls import reverse
from base.models import Room,Topic
from django.contrib.auth.models import User
from django.core.paginator import Paginator

class BaseViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        user = User.objects.create_user(username='user1',password='test12345')
        topic = Topic.objects.create(name='django')
        number_of_rooms = 13
        for room in range(number_of_rooms):
            Room.objects.create(host=user,topic=topic,name=f'test room {room}',description='hoeeeeld')

    def test_count_rooms(self):
        quantity_of_rooms = Room.objects.all().count()
        self.assertEqual(quantity_of_rooms,13)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/rooms/')
        self.assertEqual(response.status_code,200)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(reverse('base:home'))
        self.assertEqual(response.status_code,200)
    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('base:home'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'home.html')

    def test_pagination_is_three(self):
        response = self.client.get(reverse('base:home'))
        self.assertEqual(response.status_code,200)
        self.assertTrue(isinstance(response.context['page_obj'].paginator,Paginator))
    
    def test_lists_all_authors(self):
        response = self.client.get(reverse('base:home') + '?page=2')
        self.assertEqual(response.status_code,200)
        self.assertTrue(isinstance(response.context['page_obj'].paginator,Paginator))

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('base:create_room'))
        self.assertRedirects(response,'/users/login/?next=/rooms/create-room/')

    def test_login_in_uses_correct_template(self):
        login = self.client.login(username='user1',password='test12345')
        user = User.objects.get(username='user1')
        response = self.client.get(reverse('base:create_room'))
        self.assertEqual(user,response.context['user'])
        self.assertTemplateUsed(response,'create-room.html')

    def test_create_room(self):
        login = self.client.login(username='user1',password='test12345')
        user = User.objects.get(username='user1')
        response = self.client.post(reverse('base:create_room'),{'host':user,'topic':Topic.objects.all().first(),'name':'sssd'})
        print(response.url)
        rooms = Room.objects.all().count()
        print(rooms)
        
    # py manage.py test base.tests.test_views