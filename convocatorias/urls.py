from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from convocatorias import views

urlpatterns = patterns('',
    # url( r'^$', views.index, name='index' ),
    url( r'^$', 'convocatorias.views.index', name='index' ),
)