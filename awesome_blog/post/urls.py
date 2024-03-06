from django.urls import path

from .views import PostListView, PostDetailView, CommentListView, CommentDetailView, PostByTagView, CommentByTagView

urlpatterns = [
    path("posts/", PostListView.as_view()),
    path("posts/<int:pk>/", PostDetailView.as_view()),
    path('posts/by-tag/<str:tag_content>/', PostByTagView.as_view(), name='post-by-tag'),
    path("comments/post/<int:post_id>", CommentListView.as_view()),
    path("comments/<int:pk>/", CommentDetailView.as_view()),
    path('comments/by-tag/<str:tag_content>/', CommentByTagView.as_view(), name='comment-by-tag'),
]
