from django.conf.urls import url
from django.contrib.auth import login , logout
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
#from .views import  all_post,un_post
from . import   views
from django.contrib.auth.views import LoginView


#from django.contrib.auth.views import  login_required , logout_then_login
app_name = 'accounts'

"""urlpatterns = [
    url(r'^/$', views.all_post , name = 'all_post'),
    url(r'^/(?P<id>\d+)$', views.un_post , name='un_post'),
    url(r'^/form', views.form_p , name='un_post_form'),
    url('/hemidi', HomePageView.as_view(), name='home'),



]"""
urlpatterns = [

    url(r'^/$', views.hom_acc, name='accounts'),


]
#url('login/$', login_required),

#url('login/$', auth_login, {'template_name':'login.html'}),