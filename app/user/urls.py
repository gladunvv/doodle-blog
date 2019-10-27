from django.urls import path
from user.views import SignUpView, LogInView, LogOutView

app_name = 'user'
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout')
]
