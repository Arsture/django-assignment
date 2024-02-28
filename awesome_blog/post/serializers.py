from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    description = serializers.CharField(allow_blank=False, required=True)

    class Meta:
        model = Post
        fields = ['id', 'created_by', 'created_at', 'updated_at', 'title', 'description']

    def get_description(self, obj):
        return obj.description[:300]
