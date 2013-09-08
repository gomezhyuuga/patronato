from noticias.models import Noticia
from django.shortcuts import render

def index(request):
	template_name = "noticias/index.html"
	lista = Noticia.objects.order_by('created_at').reverse()

	context = { "noticias_list": lista }

	return render(request, template_name, context)
