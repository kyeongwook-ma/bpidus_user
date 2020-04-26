import phonenumbers
from rest_framework import mixins
from rest_framework import serializers
from rest_framework import status
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from user import services
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'name',
            'nickname',
            'phone_number',
            'email',
            'gender'
        )

class UserAPIView(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'email')

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():

            phone_number = serializer.data.get('phone_number')

            if not phonenumbers.is_valid_number(phone_number):
                return Response('invalid phone number', status=status.HTTP_400_BAD_REQUEST)

            services.create_user(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
