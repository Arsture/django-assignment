from rest_framework.permissions import AllowAny

from awesome_blog.pagination import CustomCursorPagination
from services.TagHandleService import tag_handle_service
from .models import Post, Comment
from .permissions import IsAuthenticated, IsOwner
from .serializers import PostDetailSerializer, PostListSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework import generics


class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostListSerializer
    pagination_class = CustomCursorPagination

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsOwner]
        return [permission() for permission in permission_classes]

    def perform_destroy(self, instance):
        tag_handle_service.delete_method_with_tag(instance)

    def perform_update(self, serializer):
        serializer.save(is_updated=True)


class CommentListView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    pagination_class = CustomCursorPagination

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        return Comment.objects.filter(post_id=post_id).order_by('-created_at')

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        serializer.save(created_by=self.request.user, post=post_id)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsOwner]
        return [permission() for permission in permission_classes]

    def perform_destroy(self, instance):
        tag_handle_service.delete_method_with_tag(instance)

    def perform_update(self, serializer):
        serializer.save(is_updated=True)


class PostByTagView(generics.ListAPIView):
    serializer_class = PostListSerializer
    pagination_class = CustomCursorPagination

    def get_queryset(self):
        return tag_handle_service.filter_by_tag(Post, self.kwargs.get('tag_content'))


class CommentByTagView(generics.ListAPIView):
    serializer_class = CommentSerializer
    pagination_class = CustomCursorPagination

    def get_queryset(self):
        return tag_handle_service.filter_by_tag(Comment, self.kwargs.get('tag_content'))
