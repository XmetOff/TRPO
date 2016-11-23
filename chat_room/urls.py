from django.conf.urls import url

from chat_room.views import CreateRoomView

urlpatterns = [url(r'^(?!.)', CreateRoomView.as_view(), name='rooms_list')]
