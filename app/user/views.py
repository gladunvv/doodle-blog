from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from user.forms import UserSignupForm, UserLoginForm
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

class SignUpView(TemplateView):

    template_name = 'user/signup.html'

    def get(self, request, *args, **kwargs):
        form = UserSignupForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        print('Пост запрос')
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}.')
            return redirect('user:login')
        return render(request, self.template_name, {'form': form})

class LogInView(TemplateView):

    template_name = 'user/login.html'

    def get(self, request, *args, **kwargs):
        form = UserLoginForm()
        return render(request, self.template_name, {'form': form})


    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Bad username or password.')
        return redirect('user:login')


class LogOut:
    def get(self, request):
        logout(request)
        return redirect("/")
