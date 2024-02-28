from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet

router = DefaultRouter()
router.register(r'', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:post_id>/comments/', include('comment.urls')),
]