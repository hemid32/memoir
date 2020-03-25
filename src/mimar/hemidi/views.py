from django.shortcuts import render
from .models import  info_tp
# Create your views here.


def all_post(request):
    all_postes = info_tp.objects.all()
    contax = {
        'all_post' : all_postes ,

    }

    return(request , 'all_p' , contax)




def un_post(request,id):

    all_postes_ = info_tp.objects.get(id=id)
    contax = {
        'all_post': all_postes_,

    }

    return (request, 'un_p', contax)

