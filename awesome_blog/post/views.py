from django.views.generic import ListView
from rest_framework import viewsets

from awesome_blog.pagination import CustomCursorPagination
from .models import Post, Comment
from .permissions import IsAdminOrOwnerOrReadOnly
from .serializers import PostSerializer, PostListSerializer, CommentListSerializer, CommentSerializer
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    pagination_class = CustomCursorPagination

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

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        return PostSerializer

    @action(detail=False, methods=['get'], url_path='by-tag/(?P<tag_content>[^/.]+)')
    def by_tag(self, request, tag_content=None):
        posts = Post.objects.filter(tags__content=tag_content)
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    pagination_class = CustomCursorPagination

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

    def get_serializer_class(self):
        if self.action == 'list':
            return CommentListSerializer
        return CommentSerializer

    @action(detail=False, methods=['get'], url_path='by-tag/(?P<tag_content>[^/.]+)')
    def by_tag(self, request, tag_content=None):
        comments = Comment.objects.filter(tags__content=tag_content)
        serializer = self.get_serializer(comments, many=True)
        return Response(serializer.data)
