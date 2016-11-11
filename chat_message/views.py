from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView
from chat_message.forms import MessageForm
from chat_room.models import Room

class ChatMessageViewSet(
        viewsets.mixins.ListModelMixin,
        viewsets.mixins.CreateModelMixin,
        viewsets.mixins.UpdateModelMixin,
        viewsets.GenericViewSet):

    def create(self, request, *args, **kwargs):
        data = request.data
        # data['author'] = request.user
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def filter_list(self, queryset, query_params):
        queryset_result = queryset.order_by('timestamp')
        chat = query_params.get('chat')
        if chat:
            queryset_result = queryset_result.filter(chat_id=chat)
        last_date_time = query_params.get('last_date_time')
        if last_date_time:
            date_time = parser.parse(last_date_time)
            queryset_result = queryset_result.filter(timestamp__gt=date_time)
        last = query_params.get('last')
        if last:
            count = queryset.count()
            fromIndex = count-int(last) if count-int(last) > 0 else 0
            queryset_result = queryset_result[fromIndex:]
        return queryset_result


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
