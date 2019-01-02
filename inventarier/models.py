from django.db import models
from django.urls import reverse

class Produkt(models.Model):
	benämning = models.CharField(max_length=255)
	tillverkare = models.CharField(max_length=255)
	modell = models.CharField(max_length=255)

	def __str__(self):
		return "{} {} {}".format(self.benämning,
			self.tillverkare,
			self.modell
		)

	class Meta:
		verbose_name_plural = "Produkter"
	
class Inventarie(models.Model):
	inventarie_nummer = models.CharField(max_length=10,unique=True)
	serienummer = models.CharField(max_length=100)
	inköpt = models.DateField() 
	rum = models.CharField(max_length=255, default='')
	aktiv = models.BooleanField(default=True)

	produkt = models.ForeignKey('Produkt',
								on_delete=models.CASCADE,
								null=True
								)

	avdelning = models.ForeignKey('Avdelning', 
								on_delete=models.CASCADE,
								related_name='avdelning_inventarier_set',
								)
	# null=True
	utlånad_till = models.ForeignKey('Avdelning',
							on_delete=models.CASCADE,
							related_name='lånade_inventarier_set',
							null=True,
							blank=True
							)

	def get_absolute_url(self):
		return reverse("inventarier:detail",
			kwargs={"inventarie_nummer": self.inventarie_nummer}
		)  

	def __str__(self):
		return str(self.inventarie_nummer)

	class Meta:
		verbose_name_plural='Inventarier'

class InventarieKommentar(models.Model):
	skapades = models.DateTimeField(auto_now_add=True)
	ämne = models.CharField(max_length=255)
	text = models.TextField()
	inventarie = models.ForeignKey('Inventarie', on_delete=models.CASCADE)
	
	def __str__(self):
		return "{} {}".format(self.ämne, self.inventarie)

	class Meta:
		verbose_name_plural = "Inventarie kommentarer"
	def get_absolute_url(self):
		return reverse("inventarier:detail",
			kwargs={"inventarie_nummer": self.inventarie.inventarie_nummer})

class Avdelning(models.Model):
	avdelning_namn = models.CharField(max_length=255)
	kostnadsställe = models.CharField(max_length=10)
	lokal = models.CharField(max_length=255)
	
	def __str__(self):
		return self.avdelning_namn

	class Meta:
		verbose_name_plural = "Avdelningar"	
