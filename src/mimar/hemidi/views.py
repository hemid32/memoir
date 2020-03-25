from django.shortcuts import render
from .models import  info_tp
# Create your views here.


def all_post(request):
    all_postes = info_tp.objects.all()
    contax = {
        'all_post' : all_postes ,

    }
    #print('hhhh')
    return render(request , 'hp.html',contax)




def un_post(request,id):
    #import pdb
    #pdb.set_trace()

    all_postes_ = info_tp.objects.get(id=id)
    contax = {
        'all_post': all_postes_,

    }

    return render(request, 'un_p.html', contax)

