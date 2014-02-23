from django.shortcuts import render
from noticias.models import Noticia
from eventos.models import Evento
from convocatorias.models import Convocatoria

def index(request):
	template_name = "patronato/index.html"
	try:
		noticia = Noticia.objects.latest()
	except Noticia.DoesNotExist:
		noticia = None
	try:
		evento = Evento.objects.latest()
	except Evento.DoesNotExist:
		evento = None
	try:
		convocatoria = Convocatoria.objects.latest()
	except Convocatoria.DoesNotExist:
		convocatoria = None
	context = { "ultima_noticia": noticia, "ultimo_evento": evento, "ultima_convocatoria": convocatoria }
	return render( request, template_name, context)

def somos(request):
	template_name = "patronato/somos.html"
	context = { }
	return render( request, template_name, context)
	
def contacto(request):
	template_name = "patronato/contacto.html"
	context = { }
	return render( request, template_name, context)