from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from user.models import Profile
from dobwidget import DateOfBirthWidget

from django.contrib.admin.widgets import AdminDateWidget


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
    years = [int(i) for i in range(1920, 2019)]
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=years))
    class Meta:
        model = Profile
        fields = ['bio', 'birth_date', 'avatar']

