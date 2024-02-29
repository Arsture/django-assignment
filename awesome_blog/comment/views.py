from rest_framework import viewsets, permissions

from .models import Comment
from post.permissions import IsAdminOrOwnerOrReadOnly
from .serializers import CommentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

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

    def perform_update(self, serializer):
        serializer.save(is_updated=True)

    @action(detail=False, methods=['get'], url_path='by-tag/(?P<tag_content>[^/.]+)')
    def by_tag(self, request, tag_content=None):
        comments = Comment.objects.filter(tags__content=tag_content)
        serializer = self.get_serializer(comments, many=True)
        return Response(serializer.data)
