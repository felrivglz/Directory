from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.index, name='index'),
    url(r'^coach/(\w+)/athletes/([a-z0-9-]+)/$', views.detail, name='detail'),
    url(r'^members/([a-z0-9-]+)/edit/$', views.edit, name='edit'),
    url(r'^coach/(\w+)/new_runner/$', views.new_runner, name='new_runner'),
    url(r'^coach/(\w+)/categoria/$', views.categoria, name='categoria'),
    url(r'^coach/(\w+)/competencia/$', views.competencia, name='competencia'),
    url(r'^coach/(\w+)/metas/([a-z0-9-]+)/$', views.metas, name='metas'),
    url(r'^coach/(\w+)/marcas/([a-z0-9-]+)/$', views.marcas, name='marcas'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^coach/(\w+)/athletes/$', views.athletes, name='athletes')
]
