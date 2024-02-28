from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'description', 'created_at', 'updated_at', 'display_tags')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'updated_at', 'tags', 'created_by')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

    def display_tags(self, obj):
        """Create a string for the Tags. This is required to display tags in List display."""
        return ', '.join([tag.content for tag in obj.tags.all()])

    display_tags.short_description = 'Tags'
