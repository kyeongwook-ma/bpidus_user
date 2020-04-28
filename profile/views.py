from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView, get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from profile.models import UserProfile
from profile.serializers import UserProfileSerializer
from user.serializers import UserLoginSerializer


class UserSearchView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'email']
    search_fields = ['name', 'email']

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)


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
