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
    """
    Courier creation API endpoint: programmatically register new couriers
    """
    # permission_classes = [permissions.IsAuthenticated]
    # pagination_class = None
    queryset = ChatMessage.objects.all()
    serializer_class = MessageSerializer

    # def get(self, request, format=None):
    #     return Response(self.queryset)

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

    def list(self, request, *args, **kwargs):
        # queryset = self.filter_queryset(self.get_queryset())
        queryset = self.filter_list(self.get_queryset(), request.query_params)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class CreateMessageView(LoginRequiredMixin, CreateView):
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
