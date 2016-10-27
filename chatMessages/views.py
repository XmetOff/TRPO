from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView

from chatMessages.forms import MessageForm
from chats.models import Chat


class CreateMessageView(CreateView):
    form_class = MessageForm
    template_name = 'chatMessages/chatmessage_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chat'] = get_object_or_404(Chat, id=self.kwargs['chat'])
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['chat'] = get_object_or_404(Chat, id=self.kwargs['chat'])
        return kwargs

    def get_success_url(self):
        return reverse('create_message', kwargs=dict(chat=self.kwargs['chat']))
