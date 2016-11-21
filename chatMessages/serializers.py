from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from django.contrib.auth.models import User
from .models import ChatMessage


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('id', 'password', 'is_superuser', 'groups', 'user_permissions',)



class MessageSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    timestamp = serializers.ReadOnlyField()
    author = UserSerializer(required=False)
    # author = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    def create(self, validated_data):
        author = self.context['request'].user
        validated_data['author'] = author
        chat_message = ChatMessage.objects.create(**validated_data)
        # chat_message.author = author
        # chat_message.save()
        return chat_message

    class Meta:
        model = ChatMessage
        exclude = ()


