from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from . import models

def create_inventarie():
	avdelning = models.Avdelning.objects.create(
				avdelning_namn="Onkologen",
				kostnadsställe="K12345",
				lokal="B:85",
			)

	inventarie = models.Inventarie.objects.create(
			inventarie_nummer='90356',
			serienummer='109hdjg33',
			inköpt=timezone.now().date(),
			avdelning=avdelning,
		)

	return inventarie

def create_inventarie_kommentar(inventarie):
	kommentar = models.InventarieKommentar.objects.create(
		ämne="Inventarie hittas ej.",
		text="Avdelning vet ej vart den är, finns ej på senast hittade rum",
		inventarie=inventarie	
	)
	
	return kommentar


class InventarieModelTests(TestCase):

	def test_inventarie_active_post_creation(self):
		""" Test för att bekräfta att inventarien är aktiv efter att den skapats """

		inventarie = create_inventarie()
		self.assertEqual(inventarie.aktiv, True)

class InventarieKommentarModelTests(TestCase):

	def test_inventarie_kommentar_creation(self):
		""" Testa att kommentaren skapas utan fördröjning """
		
		inventarie = create_inventarie()
		kommentar = create_inventarie_kommentar(inventarie)
		time_now = timezone.now()

		self.assertLess(kommentar.skapades, time_now)
		

	def test_inventarie_kommentar_inventarie(self):
		""" Test för att se om inventarie som kopplas till en kommentar har den kommentaren som skapades """

		inventarie = create_inventarie()
		kommentar = create_inventarie_kommentar(inventarie)

		self.assertIn(kommentar, inventarie.inventariekommentar_set.all())	

class InventarieViewTests(TestCase):
	
	def test_inventarie_list(self):

		""" Test för att bekräfta att inventarien dyker upp i index efter att skapats """

		inventarie = create_inventarie()	
		resp = self.client.get(reverse('inventarier:list'))		

		self.assertEqual(resp.status_code, 200)
		self.assertIn(inventarie, resp.context['inventarie_list'])
		self.assertTemplateUsed(resp, 'inventarier/inventarie_list.html')
		self.assertContains(resp, inventarie.inventarie_nummer)

	
	def test_inventaire_detail(self):
	
		""" Test för att se om relevanta data finns på sidan. """

		inventarie = create_inventarie()
		resp = self.client.get(reverse('inventarier:detail', 
			kwargs={'inventarie_nummer': inventarie.inventarie_nummer})
		)

		self.assertEqual(resp.status_code, 200)
		self.assertEqual(inventarie, resp.context['inventarie'])
		self.assertTemplateUsed(resp, 'inventarier/inventarie_detail.html')

		self.assertContains(resp, inventarie.inventarie_nummer)
		self.assertContains(resp, inventarie.serienummer)		
		self.assertContains(resp, inventarie.avdelning)		
