from django.conf.urls import url
from rest_framework_jwt.views import refresh_jwt_token

from user.views import UserLoginView, UserRegistrationView

urlpatterns = [
    url(r'^signup', UserRegistrationView.as_view()),
    url(r'^signin', UserLoginView.as_view()),
    url(r'^token/refresh', refresh_jwt_token),

]
