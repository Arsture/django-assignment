from django.contrib import admin

from comment.models import Comment
from post.models import Post
from .models import Tag


class PostInline(admin.TabularInline):
    model = Post.tags.through
    extra = 0


class CommentInline(admin.TabularInline):
    model = Comment.tags.through
    extra = 0


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('content',)
    inlines = [PostInline, CommentInline]
    search_fields = ('content',)
