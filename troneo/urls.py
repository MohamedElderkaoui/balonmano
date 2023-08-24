from django.urls import path
from .views import (
    JugadorListView,
    JugadorDetailView,
    JugadorCreateView,
    JugadorUpdateView,
    JugadorDeleteView,
    EntrenadorListView,
    EntrenadorDetailView,
    EntrenadorCreateView,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('jugadores/', JugadorListView.as_view(), name='jugador_list'),
    path('jugadores/<int:pk>/', JugadorDetailView.as_view(), name='jugador_detail'),
    path('jugadores/create/', JugadorCreateView.as_view(), name='jugador_create'),
    path('jugadores/update/<int:pk>/', JugadorUpdateView.as_view(), name='jugador_update'),
    path('jugadores/delete/<int:pk>/', JugadorDeleteView.as_view(), name='jugador_delete'),
    
    path('entrenadores/', EntrenadorListView.as_view(), name='entrenador_list'),
    path('entrenadores/<int:pk>/', EntrenadorDetailView.as_view(), name='entrenador_detail'),
    path('entrenadores/create/', EntrenadorCreateView.as_view(), name='entrenador_create'),
    # Add more URL patterns as needed
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
