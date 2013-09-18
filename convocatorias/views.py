from convocatorias.models import Convocatoria
from django.shortcuts import render

def index(request):
	template_name = "convocatorias/index.html"
	lista = Convocatoria.objects.order_by('created_at').reverse()

	context = { "convocatorias_list": lista }

	return render(request, template_name, context)