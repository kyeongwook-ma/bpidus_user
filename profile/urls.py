from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from profile.views import UserSearchView

router = DefaultRouter()
router.register(r'profiles', UserSearchView, basename='profiles')

urlpatterns = [
    path('', include(router.urls)),

]
