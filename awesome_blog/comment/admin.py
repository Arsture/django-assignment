from django.contrib import admin

from .models import Comment


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
