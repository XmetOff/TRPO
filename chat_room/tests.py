from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from chat_message.models import Message
from chat_room.models import Room


class CreateRoomViewTest(TestCase):
    def test_404(self):
        user = User.objects.create_user('user1')
        self.client.force_login(user)
        response = self.client.get(reverse('create_message', kwargs=dict(room=123)))
        self.assertEqual(response.status_code, 404)

    def test_302(self):
        creator = User.objects.create_user('user1')
        chat = Room.objects.create(name='gen', creator=creator)
        response = self.client.get(reverse('create_message', kwargs=dict(room=chat.id)))
        self.assertEqual(response.status_code, 302)

    def test_send_message(self):
        creator = User.objects.create_user('user1')
        user2 = User.objects.create_user('user2')
        chat = Room.objects.create(name='gene', creator=creator)
        self.client.force_login(user2)
        self.client.post(
            reverse('create_message', kwargs=dict(room=chat.id)),
            dict(text='weqweqwe'))
        message = Message.objects.get()
        self.assertEqual(message.text, 'weqweqwe')
        self.assertEqual(message.author, user2)

    def test_count_message(self):
        creator = User.objects.create_user('user1')
        user2 = User.objects.create_user('user2')
        chat = Room.objects.create(name='gen', creator=creator)
        self.client.force_login(user2)
        self.client.post(
            reverse('create_message', kwargs=dict(room=chat.id)),
            dict(text='weqweqwe')
        )
        self.assertEqual(Message.objects.count(), 1)

    def test_room_create(self):
        creator = User.objects.create_user('user1')
        Room.objects.create(name='gen', creator=creator)
        self.assertEqual(Room.objects.count(), 1)

    def test_creator_name_room(self):
        creator = User.objects.create_user('user1')
        chat = Room.objects.create(name='gen', creator=creator)
        self.assertEqual(chat.name, 'gen')
        self.assertEqual(chat.creator, creator)
