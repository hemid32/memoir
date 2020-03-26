from django.shortcuts import render
from .models import  info_tp
# Create your views here.
from .forme import  post_form

##$
from django.views.generic.base import TemplateView

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_post'] = info_tp.objects.all()
        return context






"""def all_post(request):
    all_postes = info_tp.objects.all()
    contax = {
        'all_post' : all_postes ,

    }
    #print('hhhh')
    return render(request , 'hp.html',contax)
"""



def un_post(request,id):
    #import pdb
    #pdb.set_trace()

    all_postes_ = info_tp.objects.get(id=id)
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
