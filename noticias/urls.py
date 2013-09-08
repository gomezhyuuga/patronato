from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from noticias import views

urlpatterns = patterns('',
    # url( r'^$', views.index, name='index' ),
    url( r'^$', 'noticias.views.index' ),
    # url( r'^noticias/', TemplateView.as_view( template_name="actividades/noticias.html" ) ),
    # url( r'^noticias/', 'actividades.views.noticias' ),
    # url( r'^eventos/', 'actividades.views.eventos' ),
    # url( r'^somos/', 'actividades.views.somos' ),
    # url( r'^contacto/', 'actividades.views.contacto' ),
    # url( r'^convocatorias/', 'actividades.views.convocatorias' ),
    # url( r'^acceso/', TemplateView.as_view( template_name="actividades/acceso.html" ) ),
)