from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils.decorators import method_decorator
from user.forms import UserSignupForm, UserLoginForm


class SignUpView(TemplateView):
    form_class = UserSignupForm
    initial = {'key': 'value'}
    template_name = 'user/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
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


class LogOutView(TemplateView):
    def get(self, request):
        logout(request)
        return redirect("/")
