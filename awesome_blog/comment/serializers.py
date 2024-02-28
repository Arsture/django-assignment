from rest_framework import serializers

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'created_by', 'created_at', 'updated_at', 'content', 'is_updated']
        read_only_fields = ['created_by', 'created_at', 'updated_at', 'is_updated']
