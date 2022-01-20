from genericpath import exists
import imp
from re import T
from urllib import response
from venv import create
from django.test import TestCase
from django.urls import reverse
from base.models import Room,Topic,Message
from django.contrib.auth.models import User
from django.core.paginator import Paginator

from base.views import room

class BaseViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = User.objects.create_user(username='user1',password='test12345')
        cls.user2 = User.objects.create_user(username='user3',password='test12345')
        cls.topic = Topic.objects.create(name='django')
        number_of_rooms = 13
        for room in range(number_of_rooms):
            Room.objects.create(host=cls.user,topic=cls.topic,name=f'test room {room}',description='hoeeeeld')

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
        user = BaseViewsTest.user
        response = self.client.get(reverse('base:create_room'))
        self.assertEqual(user,response.context['user'])
        self.assertTemplateUsed(response,'create-room.html')

    def test_created_room(self):
        self.client.login(username='user1',password='test12345')
        user = BaseViewsTest.user
        response = self.client.post(reverse('base:create_room'),{'host':user,'topic':Topic.objects.all().first(),'name':'sssd'})
        room = Room.objects.get(name='sssd')
        self.assertRedirects(response,f'/rooms/room/{room.id}/')

    def test_create_meassage_in_room_detail_page(self):
        self.client.login(username='user1',password='test12345')
        user = BaseViewsTest.user
        room = Room.objects.all().first()
        response = self.client.post(reverse('base:room',args=[room.id]),{'user':user,'room':room,'body':'this is test message'})
        self.assertRedirects(response,f'/rooms/room/{room.id}/')
        self.assertEqual(Message.objects.all().count(),1)
        

    def test_delete_message_failure(self):
        self.client.login(username='user3',password='test12345') 
        user = BaseViewsTest.user
        room = Room.objects.all().first()
        message = Message.objects.create(user=user,room=room,body='will be deleted')
        response = self.client.post(reverse('base:delete_message',kwargs={'pk':message.id}))
        self.assertNotEqual(response.status_code,302)

    
    def test_delete_message_cofirm_page_get(self):
        self.client.login(username='user1',password='test12345')
        user = BaseViewsTest.user
        room = Room.objects.all().first()
        message = Message.objects.create(user=user,room=room,body='will be deleted')
        response = self.client.get(reverse('base:delete_message',args=[message.pk]))
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.context['obj'],message)
    def test_delete_message_complete(self):
        self.client.login(username='user1',password='test12345')
        user = BaseViewsTest.user
        room = Room.objects.all().first()
        message = Message.objects.create(user=user,room=room,body='will be deleted')
        before_delete = Message.objects.all().count()
        response = self.client.post(reverse('base:delete_message',args=[message.pk]))
        self.assertEqual(before_delete - 1, Message.objects.all().count())
        self.assertEqual(response.status_code,302)
        
    

    def test_update_room_functionality_get(self):
        login = self.client.login(username='user1',password='test12345')
        user = User.objects.get(username='user1')
        room = Room.objects.filter(host=user).first()
        data = {
            'name':'updated name'
            }
        
        response = self.client.get(reverse('base:update_room',kwargs={'pk':room.id}),data)
        self.assertTemplateUsed(response,'create_update_room.html')
    
    # def test_update_room_functionality(self):
    #     login = self.client.login(username='user1',password='test12345')
    #     user = User.objects.get(username='user1')
    #     room = Room.objects.filter(host=user).first()
        
    #     response = self.client.post(reverse('base:update_room',kwargs={'pk':room.id}))
    #     self.assertTemplateUsed(response,'create_update_room.html')
    #     self.assertEqual(response.status_code,200)
    def test_update_room_functionality_failure(self):
        login = self.client.login(username='user3',password='test12345')
        
        room = Room.objects.filter(host=BaseViewsTest.user).first()
        data = {
            'name':'updated name'
            }
        response = self.client.get(reverse('base:update_room',kwargs={'pk':room.id}),data)
        self.assertTemplateNotUsed(response,'create_update_room.html')

    def test_get_delete_page(self):
        login = self.client.login(username='user1',password='test12345')
        user = BaseViewsTest.user
        topic = BaseViewsTest.topic
        room = Room.objects.create(name='Old name',host=user,topic=topic)
        response = self.client.get(reverse('base:delete_room',kwargs={'pk':room.id}))
        self.assertEqual(response.context['obj'],room)
    
    def test_delete_room_view(self): 
        login = self.client.login(username='user1',password='test12345')
        user = BaseViewsTest.user
        topic = BaseViewsTest.topic
        room = Room.objects.create(name='Old name',host=user,topic=topic)
        before_delete = Room.objects.all().count()
        response = self.client.post(reverse('base:delete_room',kwargs={'pk':room.id}))
        self.assertEqual(response.url,reverse('base:home'))
        self.assertEqual(response.status_code,302)
        after_delete = Room.objects.all().count()
        self.assertEqual(before_delete - 1,after_delete)
        self.assertRedirects(response,reverse('base:home'))
    
    def test_delete_room_view_failure(self):
        self.client.login(username='user1',password='test12345')
        new_user = User.objects.create_user(username='user2',password='test12345')
        topic = BaseViewsTest.topic
        room = Room.objects.create(name='failure test',host=new_user,topic=topic)
        response = self.client.post(reverse('base:delete_room',kwargs={'pk':room.id}))
        self.assertEqual(response.status_code,200)
        
    def test_topic_view(self):
        response = self.client.post(reverse('base:topics'))
        self.assertEqual(response.status_code,200)
        self.assertTrue(isinstance(response.context['topics'][0],Topic))
        self.assertTemplateUsed(response,'topics.html')


    def test_activities_view(self):
        response = self.client.post(reverse('base:activities'))
        Message.objects.create(user=BaseViewsTest.user,room=Room.objects.all()[0],body='dsd')
        self.assertEqual(response.status_code,200)
        self.assertTrue(isinstance(response.context['messages'][0],Message))
        self.assertTemplateUsed(response,'activity.html')
    
    
    # py manage.py test base.tests.test_views