from django.conf.urls import url

from chat_message.views import CreateMessageView

urlpatterns = [
    url(r'^(?P<room>\d)', CreateMessageView.as_view(), name='create_message')
]
