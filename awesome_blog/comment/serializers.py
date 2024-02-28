from rest_framework import serializers

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'created_by', 'content', 'created_at', 'updated_at', 'is_updated']
        read_only_fields = ('id', 'created_by', 'created_at', 'updated_at', 'is_updated')
