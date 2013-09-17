from django.shortcuts import render
from noticias.models import Noticia

def index(request):
	template_name = "patronato/index.html"
	noticia = Noticia.objects.latest('created_at')
	context = { "ultima_noticia": noticia }
	return render( request, template_name, context)
def somos(request):
	template_name = "patronato/somos.html"
	# noticia = Noticia.objects.latest('created_at')
	context = {  }
	return render( request, template_name, context)