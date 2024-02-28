from django.urls import path
from .views import PostListByTag, CommentListByTag

urlpatterns = [
    path('post', PostListByTag.as_view(), name='post-list-by-tag'),
    path('comment', CommentListByTag.as_view(), name='comment-list-by-tag'),
]
