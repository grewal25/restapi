from rest_framework import serializers
from snippets.models import Post, Choice

class PostSerializer(serializers.HyperlinkedModelSerializer):
    # choices=serializers.HyperlinkedRelatedField(
    # many=True,
    # read_only=True,
    # view_name='post-list'
    # )
    class Meta:
        model=Post
        fields=('url','pk','post_text')

class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    post=serializers.SlugRelatedField(queryset=Post.objects.all(), slug_field='post_text')
    class Meta:
        model=Choice
        fields=('url','pk','choice_text','likes','post')
