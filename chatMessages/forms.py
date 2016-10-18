from django import forms

from chatMessages.models import ChatMessage


class MessageForm(forms.ModelForm):
    class Meta:
        fields = ['text']
        model = ChatMessage

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.chat = kwargs.pop('chat', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        message = super().save(commit = False)
        message.author = self.user
        message.chat = self.chat
        message.save()
        return message