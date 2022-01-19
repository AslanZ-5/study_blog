from django.test import TestCase
from base.models import Room, Topic, Message,Profile
from django.contrib.auth.models import User
from django.urls import reverse
# Create your tests here.
class TestBase(TestCase):
    def setUp(self):
        self.user_1 = User.objects.create_user(username='user1',password='test12345')
        self.topic_1 = Topic.objects.create(name='django')
        self.room_1 = Room.objects.create(name='some test',topic=self.topic_1,host=self.user_1,description='teset room')
        self.message = Message.objects.create(room=self.room_1,user=self.user_1,body='my message')

   

    def test_profile(self):
        a = self.user_1.profile
        self.assertEqual(str(a),self.user_1.username)
        self.assertTrue(isinstance(a,Profile))

    def test_topic(self):
        a = self.topic_1
        self.assertTrue(isinstance(a,Topic))
        self.assertEqual(a.name,'django')
        self.assertEqual(str(a),'django')
    
    def test_room(self):
        d = self.room_1
        self.assertTrue(isinstance(d,Room))
        self.assertEqual(str(d),'some test')
        response = self.client.get(reverse('base:room',args=[d.pk]))
        self.assertEqual(response.status_code,200)
        r = d.get_absolute_url()
        self.assertEqual(r,f'/rooms/room/{d.id}/')

    def test_message_user(self):
        d = self.message
        self.assertEqual(len(str(d)),len('my message...'))
        self.assertEqual(d.user.username,self.user_1.username)

    def test_count_rooms(self):
        a = Room.objects.all().count()
        c = Topic.objects.all().count()
        r = User.objects.all().count()
        self.assertEquals(a,1)
        self.assertEquals(c,1)
        self.assertEquals(r,1)