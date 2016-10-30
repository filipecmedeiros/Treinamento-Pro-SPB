from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView

from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
class IndexView (TemplateView):

	template_name = 'index.html'


def contact(request):
	sucess = False
	form = ContactForm(request.POST or None)
	if form.is_valid ():
		form.send_mail()
		sucess = True
	context = {
		'forms' : form,
		'sucess' : sucess
	}
	return render(request, 'contact.html', context)
