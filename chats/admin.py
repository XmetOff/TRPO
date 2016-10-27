from django.contrib import admin

from chatMessages.admin import MessageInline
from chats.models import Chat


class ChatAdmin(admin.ModelAdmin):
    inlines = [MessageInline]


admin.site.register(Chat, ChatAdmin)
