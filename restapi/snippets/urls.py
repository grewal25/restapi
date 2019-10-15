from django.urls import path
from snippets import views

urlpatterns=[
    path('post-list/', views.PostList.as_view(), name='post-list'),
    path('post-list/<int:pk>/', views.PostDetail.as_view(),name='post-detail'),
    path('choice-list/', views.ChoiceList.as_view(), name='choice-list'),
    path('choice-list/<int:pk>/', views.ChoiceDetail.as_view(),name='choice-detail'),
    path('',views.ApiRoot.as_view(),name=views.ApiRoot.name),
]
