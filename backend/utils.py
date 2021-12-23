from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for django User
    """

    class Meta:
        model = User
        fields = (
            'id', 'username', 'first_name', 'last_name', 'is_active')


def jwt_response_payload_handler(token, user=None, request=None, issued_at=None):
    user = UserSerializer(user, context={'request': request}).data
    return {
        'token': token,
        'user': user,
    }