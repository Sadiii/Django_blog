from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from.models import Profile


class RegistrationForm(UserCreationForm):

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'type': 'email'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UpdateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']