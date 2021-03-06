"""
You are trying to use the reverse resolution of urls in Django.

In your html file correct form action url to the following and method should be POST:

<form action={% url 'process' %}  method="POST">
In case you are trying to pass parameters along then use this:

<form action={% url 'process' request.user.id 4 %}  method="POST">

"""

from django import  forms
from .models import  info_tp

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class post_form(forms.ModelForm):
    class Meta :
        Model = info_tp
        til = ['user','imail_prof']


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    your_pass = forms.CharField(label='Your pass', max_length=100)


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )