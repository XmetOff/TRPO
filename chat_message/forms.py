from django import forms

from chat_message.models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        fields = ['text']
        model = Message

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.room = kwargs.pop('room', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        message = super().save(commit=False)
        message.author = self.user
        message.room = self.room
        message.save()
        return message
