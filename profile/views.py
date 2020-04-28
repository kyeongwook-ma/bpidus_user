from django.http import JsonResponse
from rest_framework import mixins
from rest_framework import status
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.generics import RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from profile.models import UserProfile
from user.serializers import UserLoginSerializer, UserProfileSerializer


class UserProfileView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10

    def get(self, request):

        get_result = []
        name = self.request.query_params.get('name', None)
        email = self.request.query_params.get('email', None)

        if name:
            get_result.extend(list(UserProfile.objects.filter(name=name).values()))
        if email:
            get_result.extend(list(UserProfile.objects.filter(email=email).values()))

        status_code = status.HTTP_200_OK if get_result else status.HTTP_204_NO_CONTENT

        return JsonResponse(get_result, status=status_code, safe=False)


class UserSearchView(mixins.RetrieveModelMixin, mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'email')
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10


class UserLoginView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'token': serializer.data['token'],
        }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)
