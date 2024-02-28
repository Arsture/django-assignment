from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from post.models import Post
from comment.models import Comment
from post.serializers import PostSerializer
from comment.serializers import CommentSerializer


class PostListByTag(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tags__content']


class CommentListByTag(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tags__content']
