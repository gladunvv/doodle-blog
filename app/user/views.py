from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils.decorators import method_decorator
from user.forms import UserSignupForm, UserLoginForm, UserProfileForm
from django.contrib.auth import get_user_model
from doodle.models import Post
from user.models import Profile, Follow
from django.contrib.auth.mixins import LoginRequiredMixin

class UsersProfileView(LoginRequiredMixin,TemplateView):

    template_name = 'user/users_profile.html'

    def visible_user(self):
        return get_object_or_404(get_user_model(), username=self.kwargs.get('username'))

    def get(self, request, **kwargs):
        if request.user == self.visible_user():
            return redirect('user:profile')
        posts = Post.objects.filter(author=self.visible_user())
        context = {
            'profile': self.visible_user(),
            'posts': posts
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        posts = Post.objects.filter(author=self.visible_user())
        follows_between = Follow.objects.filter(following=request.user,
                                                    follower=self.visible_user())
        can_follow = (Follow.objects.filter(following=request.user,
                                                follower=self.visible_user()).count() == 0)
        if 'follow' in request.POST:
                new_relation = Follow(following=request.user, follower=self.visible_user())
                if follows_between.count() == 0:
                    new_relation.save()
        elif 'unfollow' in request.POST:
                if follows_between.count() > 0:
                    follows_between.delete()
        context = {
            'profile': self.visible_user(),
            'posts': posts,
            'can_follow': can_follow
        }
        return render(request, self.template_name, context)


class ProfileView(TemplateView):

    template_name = 'user/profile.html'
    
    def get(self, request, *args, **kwargs):
        user = request.user
        posts = Post.objects.filter(author=user).order_by('-published_date')
        context = {
            'profile': user,
            'posts': posts,
            'activate': 'profile'
        }
        return render(request, self.template_name, context)


class UpdateProfileView(TemplateView):

    template_name = 'user/update_profile.html'

    def get(self, request, *rags, **kwargs):
        user = request.user
        form = UserProfileForm()
        context = {
            'user': user,
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        user = request.user
        form_profile = UserProfileForm(request.POST, request.FILES, instance=user.profile)
        if form_profile.is_valid(): 
            form_profile.save()
            return redirect('user:profile')
        else:
            return redirect('user:profile_update')


class SignUpView(TemplateView):
    form_class = UserSignupForm
    initial = {'key': 'value'}
    template_name = 'user/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        context = {
            'form': form,
            'activate': 'signup'
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}.')
            return redirect('user:login')
        context = {
            'form': form,
            'activate': 'signup'
        }
        return render(request, self.template_name, context)


class LogInView(TemplateView):

    template_name = 'user/login.html'

    def get(self, request, *args, **kwargs):
        form = UserLoginForm()
        context = {
            'form': form,
            'activate': 'login'
        }
        return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('doodle:index')
        else:
            messages.error(request, 'Bad username or password.')
        return redirect('user:login')


class LogOutView(TemplateView):
    def get(self, request):
        logout(request)
        return redirect('user:login')


class DeleteUserView(TemplateView):
    template_name = 'user/delete_user.html'

    def get(self, request):
        user = request.user
        context = {
            'user': user
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        user = request.user
        user.delete()
        return redirect('user:signup')

class FollowsView(TemplateView):

    template_name = 'user/follow.html'

    def visible_user(self):
        return get_object_or_404(get_user_model(), username=self.kwargs.get('username'))

    def get(self, request, *args, **kwargs):
        followers = Follow.objects.filter(follower=self.visible_user()).order_by('-follow_time')
        context = {
            'followers': followers
        }
        return render(request, self.template_name, context)


class FollowersView(TemplateView):

    template_name = 'user/follow.html'

    def visible_user(self):
        return get_object_or_404(get_user_model(), username=self.kwargs.get('username'))

    def get(self, request, *args, **kwargs):
        followers = Follow.objects.filter(following=self.visible_user()).order_by('-follow_time')
        context = {
            'follows': followers
        }
        return render(request, self.template_name, context)