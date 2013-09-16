from eventos.models import Evento
from django.shortcuts import render
from django.core.mail import send_mail // Para enviar mails

def index(request):
	template_name = "eventos/index.html"
	lista = Evento.objects.order_by('created_at').reverse()

	context = { "eventos_list": lista }

	return render(request, template_name, context)

def send_contact_email(request):
	nombre = request.POST.get("nombre")
	email = request.POST.get("email")
	asunto = request.POST.get("asunto")
	mensaje = request.POST.get("mensaje")
	# Enviar mail
	# send_mail(asunto, mensaje, email, recipient_list, fail_silently=False,
		# auth_user=None, auth_password=None, connection=None, html_message=None)