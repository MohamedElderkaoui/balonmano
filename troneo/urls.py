# urls.py
from django.urls import path
from .views import JugadorListView, home,JugadorDetailView, JugadorCreateView, JugadorUpdateView, JugadorDeleteView, EntrenadorListView, EntrenadorDetailView, EntrenadorCreateView, EntrenadorUpdateView, EntrenadorDeleteView

app_name = 'jugadores'

urlpatterns = [
    path('', home, name='home'),
    
    path('jugador-list/', JugadorListView.as_view(), name='jugador-list'),
    path('jugador-list/<int:pk>/', JugadorDetailView.as_view(), name='jugador-detail'),
    path('jugador-list/create/', JugadorCreateView.as_view(), name='jugador-create'),
    path('jugador-list/<int:pk>/update/', JugadorUpdateView.as_view(), name='jugador-update'),
    path('jugador-list/<int:pk>/delete/', JugadorDeleteView.as_view(), name='jugador-delete'),
    
    path('entrenador-list/', EntrenadorListView.as_view(), name='entrenador-list'),
    path('entrenador-list/<int:pk>/', EntrenadorDetailView.as_view(), name='entrenador-detail'),
    path('entrenador-list/create/', EntrenadorCreateView.as_view(), name='entrenador-create'),
    path('entrenador-list/<int:pk>/update/', EntrenadorUpdateView.as_view(), name='entrenador-update'),
    path('entrenador-list/<int:pk>/delete/', EntrenadorDeleteView.as_view(), name='entrenador-delete'),

    # ... Other URL patterns for your app ...
]
