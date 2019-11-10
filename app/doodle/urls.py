from django.urls import path
from doodle.views import PostsListView

app_name = 'doodle'
urlpatterns = [
    path('a/', PostsListView.as_view(), name='posts'),

]
