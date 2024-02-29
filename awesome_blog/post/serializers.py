from rest_framework import serializers
from .models import Post
from tag.serializers import TagSerializer
from tag.models import Tag


class TagListField(serializers.ListField):
    child = serializers.CharField()

    def to_representation(self, value):
        # ManyRelatedManager 객체를 반복 가능한 쿼리셋으로 변환
        return [tag.content for tag in value.all()]


class PostSerializer(serializers.ModelSerializer):
    tags = TagListField()

    class Meta:
        model = Post
        fields = ['id', 'created_by', 'title', 'description', 'created_at', 'updated_at', 'tags']
        read_only_fields = ('id', 'created_by', 'created_at', 'updated_at')

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        post = Post.objects.create(**validated_data)
        for tag_name in tags_data:
            # 각 태그 이름에 대해 Tag 객체를 가져오거나 생성합니다.
            tag, created = Tag.objects.get_or_create(content=tag_name)
            post.tags.add(tag)
        return post
