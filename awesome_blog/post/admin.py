from django.contrib import admin
from .models import Post, Comment, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'description', 'created_at', 'display_tags')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'updated_at', 'tags', 'created_by')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

    def display_tags(self, obj):
        """Create a string for the Tags. This is required to display tags in List display."""
        return ', '.join([tag.content for tag in obj.tags.all()])

    display_tags.short_description = 'Tags'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'created_by', 'created_at', 'updated_at', 'display_tags')
    search_fields = ('post', 'created_by', 'tags')
    list_filter = ('created_at', 'updated_at', 'tags', 'created_by')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

    def display_tags(self, obj):
        """Create a string for the Tags. This is required to display tags in List display."""
        return ', '.join([tag.content for tag in obj.tags.all()])

    display_tags.short_description = 'Tags'


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
