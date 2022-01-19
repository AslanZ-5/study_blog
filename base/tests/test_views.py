from django.test import TestCase
from django.urls import reverse
from base.models import Room,Topic
from django.contrib.auth.models import User


class RoomListViewTest(TestCase):
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

    # py manage.py test base.tests.test_views