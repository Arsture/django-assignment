from rest_framework import serializers
from .models import Post, Comment, Tag


class TagListField(serializers.ListField):
    child = serializers.CharField()

    def to_representation(self, value):
        # ManyRelatedManager 객체를 반복 가능한 쿼리셋으로 변환
        return [tag.content for tag in value.all()]


class PostSerializer(serializers.ModelSerializer):
    tags = TagListField()

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('id', 'created_by', 'created_at', 'updated_at')

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        post = Post.objects.create(**validated_data)
        for tag_name in tags_data:
            # 각 태그 이름에 대해 Tag 객체를 가져오거나 생성합니다.
            tag, created = Tag.objects.get_or_create(content=tag_name)
            post.tags.add(tag)
        return post


class PostListSerializer(PostSerializer):
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
        tags_data = validated_data.pop('tags', [])
        comment = Comment.objects.create(**validated_data)
        for tag_name in tags_data:
            tag, created = Tag.objects.get_or_create(content=tag_name)
            comment.tags.add(tag)
        return comment


class CommentListSerializer(CommentSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'post', 'content', 'created_by', 'tags')
        read_only_fields = ('id', 'created_by')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['content']

    def create(self, validated_data):
        tag, created = Tag.objects.get_or_create(content=validated_data['content'])
        return tag
