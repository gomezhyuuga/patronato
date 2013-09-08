from eventos.models import Evento
from django.shortcuts import render

def index(request):
	template_name = "eventos/index.html"
	lista = Evento.objects.order_by('created_at').reverse()

	context = { "eventos_list": lista }

	return render(request, template_name, context)
