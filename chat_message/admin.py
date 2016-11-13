from django.contrib import admin

from chat_message.models import Message


class MessageInline(admin.TabularInline):
    model = Message


admin.site.register(Message)

# Register your models here.
