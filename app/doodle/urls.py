from django.urls import path
from doodle.views import PostsListView, PostDetailView, CreatePost

app_name = 'doodle'
urlpatterns = [
    path('', PostsListView.as_view(), name='index'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/create', CreatePost.as_view(), name='create_post')
]
