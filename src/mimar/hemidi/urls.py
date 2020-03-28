from django.conf.urls import url

#from .views import  all_post,un_post
from .views import  un_post , pag_post
from . import   views
from .views import  HomePageView
app_name = 'hemidi'

"""urlpatterns = [
    url(r'^/$', views.all_post , name = 'all_post'),
    url(r'^/(?P<id>\d+)$', views.un_post , name='un_post'),
    url(r'^/form', views.form_p , name='un_post_form'),
    url('/hemidi', HomePageView.as_view(), name='home'),



]"""
urlpatterns = [

    url(r'^/(?P<id>\d+)$', un_post , name='un_post'),
    url(r'form', pag_post , name='un_post_form'),
    url(r'^/$', views.all_post, name='home'),
    url(r'^/login/$',  views.get_name, name='login'),
    url(r'^/signup/$', views.signup, name='signup'),


]
