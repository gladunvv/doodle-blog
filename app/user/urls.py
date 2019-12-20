from django.urls import path
from user.views import SignUpView, LogInView, LogOutView, ProfileView, UpdateProfileView, DeleteUserView

app_name = 'user'
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('delete/', DeleteUserView.as_view(), name='delete'),
    path('profile/update', UpdateProfileView.as_view(), name='profile_update')
]
