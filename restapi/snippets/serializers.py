from rest_framework import serializers
from snippets.models import Post, Choice

class PostSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model=Post
        fields=('url','id','post_text')

class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    post=serializers.SlugRelatedField(queryset=Post.objects.all(), slug_field='post_text')
    class Meta:
        model=Choice
        fields=('id','choice_text','likes','post')
