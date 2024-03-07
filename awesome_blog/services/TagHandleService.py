from openid.consumer.consumer import Response

from post.models import Tag


class TagHandleService:

    def create_object_with_tag(self, validated_data, object):
        tags_data = validated_data.pop('tags', [])
        made_object = object.objects.create(**validated_data)
        for tag_name in tags_data:
            tag, created = Tag.objects.get_or_create(content=tag_name)
            made_object.tags.add(tag)
        return made_object

    def delete_method_with_tag(self, instance):
        tags = instance.tags.all()

        for tag in tags:
            if tag.comments.count() + tag.posts.count() == 1:
                tag.delete()

        instance.delete()

    def filter_by_tag(self, object, tag_content):
        return object.objects.filter(tags__content=tag_content).order_by('-created_at')


tag_handle_service = TagHandleService()
