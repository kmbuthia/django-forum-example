from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField
from decouple import config

class SignupForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    captcha = ReCaptchaField()