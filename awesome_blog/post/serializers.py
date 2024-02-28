from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'created_by', 'title', 'description', 'created_at', 'updated_at']
        read_only_fields = ('id', 'created_by', 'created_at', 'updated_at')
