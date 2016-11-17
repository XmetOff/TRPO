from django.conf.urls import url

from .views import IndexView

urlpatterns = [
    url('^(?P<pk>\d+)', IndexView.as_view(), name='chat')
]
