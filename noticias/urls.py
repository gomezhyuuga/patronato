from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from noticias import views

urlpatterns = patterns('',
    # url( r'^$', views.index, name='index' ),
    url( r'^$', 'noticias.views.index', name='index' ),
)