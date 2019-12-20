from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from user.models import Profile


class UserSignupForm(UserCreationForm):

    email = forms.EmailField()
    first_name = forms.CharField(max_length=15)
    last_name = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1']


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']


class UserProfileForm(forms.ModelForm):

    birth_date = forms.DateField(label='Birthday', widget=forms.SelectDateWidget)
    
    class Meta:
        model = Profile
        fields = ['bio', 'birth_date']
