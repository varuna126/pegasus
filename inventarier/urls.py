from django.urls import path
from . import views

app_name = 'inventarier'

urlpatterns = [
	path('', views.InventarieListView.as_view(), name='list'),
	path('ny/', views.InventarieCreate.as_view(), name='create'),
	path('<inventarie_nummer>/action/', views.InventarieKommentarCreate.as_view(), name='create_kommentar'),
	path('<inventarie_nummer>/redigera/', views.InventarieUpdate.as_view(),
		name='update'), 
	path('<inventarie_nummer>/', views.InventarieDetailView.as_view(), 
		name='detail'),
]
