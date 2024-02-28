from django.urls import path, include
from rest_framework import routers

from .views import CommentViewSet

router = routers.SimpleRouter()
router.register(r'', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # 여기에 더 많은 comment 관련 URL 패턴을 추가할 수 있습니다.
]
