from rest_framework import serializers
from .models import Post
from tag.serializers import TagSerializer
from tag.models import Tag


class PostSerializer(serializers.ModelSerializer):
    description = serializers.CharField(allow_blank=False, required=True)
    tags = serializers.ListField(
        child=serializers.CharField(),
        required=False
    )

    class Meta:
        model = Post
        fields = '__all__'

    def get_description(self, obj):
        return obj.description[:300]

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        print(tags_data)
        post = Post.objects.create(**validated_data)
        print(post)
        for tag_name in tags_data:
            tag, created = Tag.objects.get_or_create(content=tag_name)
            print(tag, created)
            post.tags.add(tag)
        return post

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', [])
        instance = super().update(instance, validated_data)

        if tags_data:
            instance.tags.clear()
            for tag_name in tags_data:
                tag, created = Tag.objects.get_or_create(content=tag_name)
                instance.tags.add(tag)

        return instance
