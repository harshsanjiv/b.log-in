from django.urls import path
from .views import PostDetailView,PostListView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView,CommentListView,CommentCreateView
from . import views
urlpatterns=[
    path('',PostListView.as_view(),name="blog-home"),
    path('about/',views.about,name="blog-about"),
    path('post/<int:pk>/',PostDetailView.as_view(),name="post-detail"),
    path('post/<int:pk>/',CommentListView.as_view(),name="comment-detail"),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/comment/new/',CommentCreateView.as_view(),name="comment-create"),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name="post-update"),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name="post-delete"),
    path('user/<str:username>/',UserPostListView.as_view(),name="user-posts"),
    
]