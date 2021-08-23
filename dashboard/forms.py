from django import forms
from .models import User_staff
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'style':'height:50px'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'style':'height:50px'}))


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = get_user_model()
        fields = ('username',  'password1', 'password2')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = '__all__'

