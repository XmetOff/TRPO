from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView

from chat_message.forms import MessageForm
from chat_room.models import Room


# Create your views here.

class CreateMessageView(LoginRequiredMixin, CreateView):
    form_class = MessageForm
    template_name = 'chat_message/message_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['room'] = get_object_or_404(Room, id=self.kwargs['room'])
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['room'] = get_object_or_404(Room, id=self.kwargs['room'])
        return kwargs

    def get_success_url(self):
        return reverse('create_message', kwargs=dict(room=self.kwargs['room']))
