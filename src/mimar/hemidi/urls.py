from django.conf.urls import url

#from .views import  all_post,un_post
#from .views import  all_post , un_post
from . import   views
app_name = 'hemidi'

urlpatterns = [
    url(r'^/$', views.all_post , name = 'all_post'),
    url(r'^/(?P<id>\d+)$', views.un_post , name='un_post')]