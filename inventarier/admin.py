from django.contrib import admin
from . import models 

admin.site.register(models.Inventarie)
admin.site.register(models.InventarieKommentar)
admin.site.register(models.Produkt)
admin.site.register(models.Avdelning)

