from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
	ListView, DetailView, 
	CreateView, UpdateView, 
	DeleteView
)

from .models import Inventarie, InventarieKommentar


class InventarieListView(ListView):
	model = Inventarie

class InventarieDetailView(DetailView):
	model = Inventarie
	slug_url_kwarg = 'inventarie_nummer'
	slug_field = 'inventarie_nummer'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		if self.object.aktiv == True:
			action = "Inaktivera"
		else:
			action = "Aktivera"
		context['action'] = action
		return context

class InventarieCreate(CreateView):
	model = Inventarie
	fields = ['inventarie_nummer', 'serienummer', 'rum', 'inköpt', 'produkt', 'avdelning', 'utlånad_till']

class InventarieUpdate(UpdateView):
	model = Inventarie
	fields = ['inventarie_nummer', 'serienummer', 'rum', 'inköpt', 'produkt', 'avdelning', 'utlånad_till']

	def get_object(self):
		return get_object_or_404(Inventarie, inventarie_nummer=self.kwargs['inventarie_nummer'])
	
class InventarieKommentarCreate(CreateView):
	model = InventarieKommentar
	fields = ['text', ]

#	def get_initial(self):
#		initial = super().get_initial()	
#		initial['text'] = 'hejsan'
#		inventarie = get_object_or_404(Inventarie, 
#			inventarie_nummer=self.kwargs['inventarie_nummer'])
#		initial['inventarie'] = inventarie
#		if isinstance(initial['inventarie'], Inventarie):
#			print("is correct instance")
#		return initial

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		inventarie = get_object_or_404(Inventarie,
			inventarie_nummer=self.kwargs['inventarie_nummer'])
		context['inventarie'] = inventarie 

		if inventarie.aktiv == True:
			action = "Inaktivera"
		else:
			action = "Aktivera"
		context['action'] = action

		return context

	def form_valid(self, form):
		inventarie_kommentar = form.instance
		inventarie_kommentar.inventarie = get_object_or_404(Inventarie,
			inventarie_nummer=self.kwargs['inventarie_nummer'])

		if inventarie_kommentar.inventarie.aktiv == True:
			inventarie_kommentar.inventarie.aktiv = False
			ämne = "Inaktivering av Inventarie"
			print("Inventarie inaktiveras")
		else:
			inventarie_kommentar.inventarie.aktiv = True
			ämne = "Aktivering av Inventarie"
			print("Inventarie aktiveras")

		inventarie_kommentar.ämne = ämne
		inventarie_kommentar.inventarie.save()	

		return super().form_valid(form)
