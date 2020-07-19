from django.contrib import admin
from django.urls import include, path
from Insta.views import (HelloWorld, EditProfile,
toggleFollow,UserDetailView, addLike, PostDeleteView, addComment, ExploreView,
PostUpdateView, PostCreateView, PostsView, PostDetailView)
from . import views


urlpatterns = [
    path('helloworld', HelloWorld.as_view(), name = 'helloworld'),
    path('', PostsView.as_view(), name = 'posts'),
    path('posts/<int:pk>', PostDetailView.as_view(), name = 'post_detail'),
    path('posts/new/', PostCreateView.as_view(), name = 'make_post'),
    path('posts/update/<int:pk>', PostUpdateView.as_view(), name = 'update_post'),
    path('posts/delete/<int:pk>', PostDeleteView.as_view(), name = 'delete_post'),
    path('like', addLike, name='addLike'),
    path('user/<int:pk>', UserDetailView.as_view(), name = 'user_detail'),
    path('togglefollow', toggleFollow, name='togglefollow'),
    path('edit_profile/<int:pk>/', EditProfile.as_view(), name='edit_profile'),
    path('comment', addComment, name='addComment'),
    path('explore', ExploreView.as_view(), name='exploreusers'),
]
