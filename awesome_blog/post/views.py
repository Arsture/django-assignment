from rest_framework import viewsets
from .models import Post
from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsOwnerOrReadOnly]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=False, methods=['get'], url_path='by-tag/(?P<tag_content>[^/.]+)')
    def by_tag(self, request, tag_content=None):
        posts = Post.objects.filter(tags__content=tag_content)
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)
