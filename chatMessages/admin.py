from django.contrib import admin

from chatMessages.models import ChatMessage


class MessageInline(admin.TabularInline):
    model = ChatMessage


admin.site.register(ChatMessage)
