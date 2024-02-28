from rest_framework import serializers
from tag.serializers import TagSerializer
from tag.models import Tag

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'created_by', 'content', 'created_at', 'updated_at', 'is_updated', 'tags']
        read_only_fields = ('id', 'created_by', 'created_at', 'updated_at', 'is_updated')

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        comment = Comment.objects.create(**validated_data)
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(content=tag_data['content'])
            comment.tags.add(tag)
        return comment
