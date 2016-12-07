from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from chatMessages.models import ChatMessage
from chat_room.models import Chat


class CreateMessageViewTest(TestCase):
    def test_404(self):
        user = User.objects.create_user('user1')
        self.client.force_login(user)
        response = self.client.get(reverse('create_message', kwargs=dict(chat=123)))
        self.assertEqual(response.status_code, 404)

    def test_302(self):
        creator = User.objects.create_user('user1')
        chat = Chat.objects.create(name='general', creator=creator)
        response = self.client.get(reverse('create_message', kwargs=dict(chat=chat.id)))
        self.assertEqual(response.status_code, 302)

    def test_send_message(self):
        creator = User.objects.create_user('user1')
        user2 = User.objects.create_user('user2')
        chat = Chat.objects.create(name='general', creator=creator)
        self.client.force_login(user2)
        self.client.post(
            reverse('create_message', kwargs=dict(chat=chat.id)),
            dict(text='weqweqwe')
        )
        message = ChatMessage.objects.get()
        self.assertEqual(message.text, 'weqweqwe')
        self.assertEqual(message.author, user2)

    def test_count_message(self):
        creator = User.objects.create_user('user1')
        user2 = User.objects.create_user('user2')
        chat = Chat.objects.create(name='general', creator=creator)
        self.client.force_login(user2)
        self.client.post(
            reverse('create_message', kwargs=dict(chat=chat.id)),
            dict(text='weqweqwe')
        )
        self.assertEqual(ChatMessage.objects.count(), 1)
