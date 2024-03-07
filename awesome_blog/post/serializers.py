from rest_framework import serializers

from services.TagHandleService import tag_handle_service
from .models import Post, Comment, Tag


class TagListField(serializers.ListField):
    child = serializers.CharField()

    def to_representation(self, value):
        # ManyRelatedManager 객체를 반복 가능한 쿼리셋으로 변환
        return [tag.content for tag in value.all()]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['content']

    def create(self, validated_data):
        tag, created = Tag.objects.get_or_create(content=validated_data['content'])
        return tag


class PostDetailSerializer(serializers.ModelSerializer):
    tags = TagListField()

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('id', 'created_by', 'created_at', 'updated_at')

    def create(self, validated_data):
        return tag_handle_service.create_object_with_tag(validated_data, Post)


class PostListSerializer(PostDetailSerializer):
    class Meta:
        model = Post
        fields = ['id', 'created_by', 'title', 'description', 'tags']
        read_only_fields = ('id', 'created_by')


class CommentSerializer(serializers.ModelSerializer):
    tags = TagListField()

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('id', 'created_by', 'created_at', 'updated_at', 'is_updated')

    def create(self, validated_data):
        return tag_handle_service.create_object_with_tag(validated_data, Comment)
