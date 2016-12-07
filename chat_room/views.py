from django.views.generic.detail import SingleObjectMixin
from django.views.generic import DetailView
from rest_framework import viewsets
from rest_framework import permissions
from .models import Chat


# class CourierViewSet(
#         viewsets.mixins.ListModelMixin,
#         viewsets.mixins.CreateModelMixin,
#         viewsets.mixins.UpdateModelMixin,
#         viewsets.GenericViewSet):
#     """
#     Courier creation API endpoint: programmatically register new couriers
#     """
#     permission_classes = [permissions.IsAdminUser]
#     pagination_class = None
#     queryset = Courier.objects.all()
#     serializer_class = CourierSerializer


class IndexView(DetailView, SingleObjectMixin):
    template_name = 'index.html'
    model = Chat
