from django.shortcuts import render
from noticias.models import Noticia

def index(request):
	template_name = "patronato/index.html"
	try:
		noticia = Noticia.objects.latest()
	except Noticia.DoesNotExist:
		noticia = None
	context = { "ultima_noticia": noticia }
	return render( request, template_name, context)

def somos(request):
	template_name = "patronato/somos.html"
	context = { }
	return render( request, template_name, context)
	
def contacto(request):
	template_name = "patronato/contacto.html"
	context = { }
	return render( request, template_name, context)