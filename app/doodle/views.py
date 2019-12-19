from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from doodle.models import Post, Comment, Tag
from user.models import Follow
from django.contrib.auth import get_user_model
from doodle.forms import AddCommentForm, AddPost

class PostsListView(ListView):

    template_name = 'doodle/index.html'

    def get(self, request):
        user = request.user
        followers = user.who_follows.all()
        follow_list = [user]
        for f in followers:
            follow_list.append(f.follower)
        posts = Post.objects.filter(author__in=follow_list).order_by('-published_date')
        context = {
            'posts': posts,
            'activate': 'index'
        }
        return render(request, self.template_name, context)    


class PostDetailView(TemplateView):

    template_name = 'doodle/post_detail.html'

    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = AddCommentForm()
        context = {
            'post': post,
            'add_comment': form
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = AddCommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            comment = Comment(
                text=text, author=request.user, post=post)
            comment.save()
            form = AddCommentForm()
        context = {
            'post': post,
            'add_comment': form
        }
        return render(request, self.template_name, context)


class CreatePost(TemplateView):

    template_name = 'doodle/added_post.html'

    def get(self, request):
        form = AddPost()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        user = request.user
        form = AddPost(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            post = Post(
                text=text, author=user
            )
            post.published()
            post.save()
            return redirect('user:profile')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
