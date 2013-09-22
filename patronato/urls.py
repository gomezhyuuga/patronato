from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
# from patronato.admin import patronato_admin_site # admin del cliente

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', TemplateView.as_view(template_name="patronato/index.html") ),
    url(r'^$', "patronato.views.index", name="index" ),
    # url(r'^patronato/', include('patronato.foo.urls')),
    url(r'^noticias/', include('noticias.urls', namespace='noticias')),
    url(r'^eventos/', include('eventos.urls', namespace='eventos')),
    url(r'^convocatorias/', include('convocatorias.urls', namespace='convocatorias')),
    url(r'^somos/', "patronato.views.somos", name="somos"),
    url(r'^contacto/', "patronato.views.contacto", name="contacto"),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^gestion/', include(patronato_admin_site.urls)),
)
