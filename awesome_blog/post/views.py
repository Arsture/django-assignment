from rest_framework import viewsets
from .models import Post
from .permissions import IsAdminOrOwnerOrReadOnly
from .serializers import PostSerializer
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminOrOwnerOrReadOnly]
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
