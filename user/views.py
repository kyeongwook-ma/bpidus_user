from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from user.serializers import UserLoginSerializer, UserRegistrationSerializer


class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'message': 'User registered  successfully'
        }, status=status.HTTP_200_OK)


class UserLoginView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'message': 'User logged in  successfully',
            'token': serializer.data['token'],
        }

        return Response(response, status=status.HTTP_200_OK)
