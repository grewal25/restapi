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






# class PostList(APIView):
#     def get(self, request, format=None):
#         posts=Post.objects.all()
#         serializer=PostSerializer(posts, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer=PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# class PostDetail


# class ChoiceList(APIView):
#     def get(self, request, format=None):
#         choices=Choice.objects.all()
#         posts=Post.objects.all()
#         serializer1=ChoiceSerializer(choices, many=True)
#         serializer2=PostSerializer(posts, many=True)
#         return Response(serializer2.data)

    # def post(self, request, format=None):
    #     serializer=ChoiceSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
