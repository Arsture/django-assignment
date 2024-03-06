from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet

router = DefaultRouter() #TODO: router 쓰지말자
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
