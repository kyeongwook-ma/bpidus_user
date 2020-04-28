from rest_framework import serializers

from profile.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('name', 'nickname', 'phone_number', 'email', 'gender')
