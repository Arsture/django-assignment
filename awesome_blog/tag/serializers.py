from rest_framework import serializers
from .models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['content']

    def create(self, validated_data):
        tag, created = Tag.objects.get_or_create(content=validated_data['content'])
        return tag
