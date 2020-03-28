from django.shortcuts import render
# Create your views here.
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
#from .forms import NameForm
from .forms import  NameForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import  SignUpForm



def hom_acc(request):

    return render(request, 'lo.html')


