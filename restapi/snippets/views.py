from django.shortcuts import render
from rest_framework import generics
from rest_framework.reverse import reverse
from .models import Choice, Post
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from snippets.serializers import ChoiceSerializer, PostSerializer

class PostList(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    name='post-list'

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    name='post-detail'

class ChoiceList(generics.ListCreateAPIView):
    queryset=Choice.objects.all()
    serializer_class=ChoiceSerializer
    name='choice-list'

class ChoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Choice.objects.all()
    serializer_class=ChoiceSerializer
    name='choice-detail'

class ApiRoot(generics.GenericAPIView):
    name='api-root'

    def get(self, request, *args, **kwargs):
        return Response({
        'posts': reverse(PostList.name, request=request),
        'choices': reverse(ChoiceList.name, request=request),
        })
