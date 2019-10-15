from rest_framework import serializers
from snippets.models import Post, Choice

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Post
        fields=['id','post_text']

class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Choice
        fields=['id','choice_text','likes']
