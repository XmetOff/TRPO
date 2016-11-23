from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

from chat_room.models import Room


# Create your views here.

class CreateRoomView(LoginRequiredMixin, CreateView):
    model = Room
    template_name = "chat_room/room_create_bootsrtap.html"
    fields = ['name']
    success_url = '/roms'

    def get_context_data(self, **kwargs):
        context = super(CreateRoomView, self).get_context_data(**kwargs)
        context['objects'] = self.model.objects.all()
        return context

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super(CreateRoomView, self).form_valid(form)
