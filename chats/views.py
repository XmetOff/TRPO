from django.views.generic.detail import SingleObjectMixin
from django.views.generic import DetailView
from .models import Chat


class IndexView(DetailView, SingleObjectMixin):
    template_name = 'index.html'
    model = Chat
