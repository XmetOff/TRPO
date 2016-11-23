from django.contrib import admin

from chat_message.admin import MessageInline
from chat_room.models import Room


class RoomAdmin(admin.ModelAdmin):
    inlines = [MessageInline]


admin.site.register(Room, RoomAdmin)
