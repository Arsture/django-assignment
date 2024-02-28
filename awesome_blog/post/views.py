from rest_framework import viewsets, permissions
from .models import Post
from .serializers import PostSerializer
from .permissions import IsOwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing posts.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_object(self):
        post = super().get_object()
        # 여기에 필요한 로직을 추가할 수 있습니다.
        return post
