from django.urls import path
from doodle.views import PostsListView

app_name = 'doodle'
urlpatterns = [
    path('index/', PostsListView.as_view(), name='posts'),

]
