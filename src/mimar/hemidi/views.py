from django.shortcuts import render
from .models import  info_tp
# Create your views here.
from .forme import  post_form
import serial
from time import sleep
##$
from django.views.generic.base import TemplateView
from django.contrib.auth import login, authenticate
from django.shortcuts import render
# Create your views here.
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forme import  NameForm
from django.contrib.auth import login, authenticate , user_logged_in
from django.shortcuts import render, redirect
from .forme import  SignUpForm
from django.contrib.auth import logout
from django.contrib.auth.models import User
#from articles.models import Article
"""
You are trying to use the reverse resolution of urls in Django.

In your html file correct form action url to the following and method should be POST:

<form action={% url 'process' %}  method="POST">
In case you are trying to pass parameters along then use this:

<form action={% url 'process' request.user.id 4 %}  method="POST">

"""



class HomePageView(TemplateView):

    template_name = "hp.html"

    def get_context_data(self, request,**kwargs):

        # Redirect to a success page.
        if request.user.is_active :

            print('yess')
        else :
            print('nnnn')

        context = super().get_context_data(**kwargs)
        context['all_post'] = info_tp.objects.all()
        return context






def all_post(request):

    if request.user.is_active:
        all_postes = info_tp.objects.all()
        contax = {
            'all_post' : all_postes ,

        }
        #print('hhhh')
        return render(request , 'hp.html',contax)
    else :
        return  redirect('/home/login/')




def un_post(request,id):
    #import pdb
    #pdb.set_trace()


    all_postes_ = info_tp.objects.get(id=id)
    #print(all_postes_.type_shm)
    contax = {
        'all_post': all_postes_,

    }


    return render(request, 'un_p.html', contax)





def pag_post(request,id):
    #import pdb
    #pdb.set_trace()
    #print(id)


    all_postes_ = info_tp.objects.get(id=id)


    contax = {
        'all_post': all_postes_,

    }

    return render(request, 'post_info.html', contax)

"""def form_p(request) :
    if  request.method == 'POST' :
        form = post_form(request.post)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
    else :
        form = post_form()

    contax = {'form' : form ,}

    return  render(request , 'form.html' , contax)
"""
def arduino_g(n) :
    ser = serial.Serial('/dev/ttyUSB0', baudrate=9600,
                        bytesize=serial.EIGHTBITS,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        timeout=1,
                        xonxoff=0,
                        rtscts=0
                        )
    counter = 0

    n = bytes(str(n),'utf-8')

    ser.write(n)

    if counter == 255:
        with ser:  # the reset part is actually optional but the sleep is nice to have either way.
            ser.setDTR(False)
            sleep(1)
            ser.flushInput()
            ser.setDTR(True)

def get_name(request):
    logout_view(request)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            username = request.POST['your_name']
            password = request.POST['your_pass']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page.

                print('yess')
                m = HomePageView
                return  redirect('/home/')

            else:
                # Return an 'invalid login' error message.
                print('non')
                #pass

            #print(password)
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'login.html', {'form': form})


def signup(request):
    logout_view(request)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/home/login/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
def logout_view(request):
    logout(request)
    # Redirect to a success page.
    redirect('/home/login/')