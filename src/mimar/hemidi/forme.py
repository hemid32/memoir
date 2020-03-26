"""
You are trying to use the reverse resolution of urls in Django.

In your html file correct form action url to the following and method should be POST:

<form action={% url 'process' %}  method="POST">
In case you are trying to pass parameters along then use this:

<form action={% url 'process' request.user.id 4 %}  method="POST">

"""

from django import  forms
from .models import  info_tp

class post_form(forms.ModelForm):
    class Meta :
        Model = info_tp
        til = ['user','imail_prof']