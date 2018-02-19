from django.conf.urls import url
from .import views




app_name= 'blog'

urlpatterns = [

    url(r'^$', views.home, name='home'),
     url(r'^lectures/$', views.lecture, name='lectures'),


]
