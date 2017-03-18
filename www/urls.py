from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.index, name='index'),
    url(r'^members/([a-z0-9-]+)/$', views.detail, name='detail'),
    url(r'^members/([a-z0-9-]+)/edit/$', views.edit, name='edit'),
    url(r'^members/new_runner/$', views.new_runner, name='new_runner'),
    url(r'^members/([a-z0-9-]+)/metas/$', views.metas, name='metas'),
]
