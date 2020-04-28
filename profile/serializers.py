from django.contrib.auth.models import User

from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'nickname', 'phone_number', 'email', 'gender')
