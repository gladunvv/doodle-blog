from django.shortcuts import render
from django.views.generic import ListView
from doodle.models import Post, Comment, Tag
from user.models import Follow
from django.contrib.auth import get_user_model

class PostsListView(ListView):

    template_name = 'doodle/index.html'

    def get(self, request):
        user = get_user_model().objects.get(username='vlad')
        followers = user.who_follows.all()
        follow_list = [user]
        for f in followers:
            follow_list.append(f.follower)
        posts = Post.objects.filter(author__in=follow_list).order_by('-published_date')
        data = {
            'posts': posts,
        }
        return render(request, self.template_name, data)    
