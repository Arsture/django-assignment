from rest_framework import serializers
from .models import Post
from tag.serializers import TagSerializer
from tag.models import Tag


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = ['id', 'created_by', 'title', 'description', 'created_at', 'updated_at', 'tags']
        read_only_fields = ('id', 'created_by', 'created_at', 'updated_at')

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        post = Post.objects.create(**validated_data)
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(content=tag_data['content'])
            post.tags.add(tag)
        return post
