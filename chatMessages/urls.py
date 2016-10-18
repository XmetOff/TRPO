from django.conf.urls import url

from chatMessages.views import CreateMessageView

urlpatterns = [
    url('^(?P<chat>\d+)', CreateMessageView.as_view(), name = 'create_message')
]

