from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import jugador
from .tables import JugadorTable, entrenadorTable
from django.shortcuts import render
from .forms import JugadorForm, EntrenadorForm, EquipoForm, PartidoForm
from django_tables2 import SingleTableView, SingleTableMixin
from django_tables2.export.views import ExportMixin
# jsonresponse
from django.http import JsonResponse
# importamos el serialized 
from django.core.serializers import serialize
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required



from .models import *
from .forms import *
from .admin import *
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import jugador, entrenador, Equipo, Partido, clasificacion, relacion_entre_jugadores_y_equipos, relacion_entre_entrenadores_y_equipos, relacion_entre_equipos_y_partidos
from .forms import JugadorForm, EntrenadorForm, EquipoForm, PartidoForm
from django.http import JsonResponse

def home(request):
    return render(request, 'troneo/home.html')

class JugadorListView(ListView):
    model = jugador
    table_class = JugadorTable
    form_class = JugadorForm
    template_name = 'jugadores/jugador_list.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        table = JugadorTable(jugador.objects.all())
        table.paginate(page=self.request.GET.get("page", 1), per_page=10)
        context["table"] = table
        
        return context

# wirh pk of the object jugadores/<pk>
class JugadorDetailView(DetailView):
    model = jugador
    template_name = 'jugadores/jugador_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        jugador_object = jugador.objects.get(pk=self.kwargs['pk'])# Get the jugador object
        data = {
            'nombre': jugador_object.nombre,
            'apellido': jugador_object.apellido,
            'edad': jugador_object.edad,
            'posicion': jugador_object.posicion,
            'nacionalidad': jugador_object.nacionalidad,
            'foto': jugador_object.foto.url,
        }
        # save on json serialized for javascript dom
        context['data'] = serialize('json', [jugador_object,], fields=('nombre', 'apellido', 'edad', 'posicion', 'nacionalidad', 'foto'))
        context['url'] = jugador_object.foto.url
        return context
class JugadorCreateView(View):
    def get(self, request):
        form = JugadorForm()
        return render(request, 'jugadores/jugador_form.html', {'form': form})
    
    def post(self, request):
        form = JugadorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('jugador_list')
        return render(request, 'jugadores/jugador_form.html', {'form': form})

class JugadorUpdateView(View):
    def get(self, request, pk):
        player = get_object_or_404(jugador, pk=pk)
        form = JugadorForm(instance=player)
        return render(request, 'jugadores/jugador_form.html', {'form': form})
    
    def post(self, request, pk):
        player = get_object_or_404(jugador, pk=pk)
        form = JugadorForm(request.POST, request.FILES, instance=player)
        if form.is_valid():
            form.save()
            return redirect('jugador_list')
        return render(request, 'jugadores/jugador_form.html', {'form': form})

class JugadorDeleteView(View):
    def get(self, request, pk):
        player = get_object_or_404(jugador, pk=pk)
        return render(request, 'jugadores/jugador_confirm_delete.html', {'player': player})
    
    def post(self, request, pk):
        player = get_object_or_404(jugador, pk=pk)
        player.delete()
        return redirect('jugador_list')

class EntrenadorListView(ListView):
    model = entrenador
    table_class = entrenadorTable
    form_class = EntrenadorForm
    template_name = 'entrenadores/entrenador_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        table = entrenadorTable(entrenador.objects.all())
        table.paginate(page=self.request.GET.get("page", 1), per_page=10)
        context["table"] = table
        
        return context
    
class EntrenadorDetailView(DetailView):
    model = entrenador
    template_name = 'entrenadores/entrenador_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        entrenador_object = entrenador.objects.get(pk=self.kwargs['pk'])# Get the entrenador object
        data = {
            'nombre': entrenador_object.nombre,
            'apellido': entrenador_object.apellido,
            'edad': entrenador_object.edad,
            'nacionalidad': entrenador_object.nacionalidad,
            'foto': entrenador_object.foto.url,
        }
        # save on json serialized for javascript dom
        context['data'] = serialize('json', [entrenador_object,], fields=('nombre', 'apellido', 'edad', 'nacionalidad', 'foto'))
        context['url'] = entrenador_object.foto.url
        return context
    
class EntrenadorCreateView(View):
    def get(self, request):
        form = EntrenadorForm()
        return render(request, 'entrenadores/entrenador_form.html', {'form': form})
    
    def post(self, request):
        form = EntrenadorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('entrenador_list')
        return render(request, 'entrenadores/entrenador_form.html', {'form': form})
    
class EntrenadorUpdateView(View):
    def get(self, request, pk):
        entrenador_object = get_object_or_404(entrenador, pk=pk)
        form = EntrenadorForm(instance=entrenador_object)
        return render(request, 'entrenadores/entrenador_form.html', {'form': form})
    
    def post(self, request, pk):
        entrenador_object = get_object_or_404(entrenador, pk=pk)
        form = EntrenadorForm(request.POST, request.FILES, instance=entrenador_object)
        if form.is_valid():
            form.save()
            return redirect('entrenador_list')
        return render(request, 'entrenadores/entrenador_form.html', {'form': form})

class EntrenadorDeleteView(View):
    def get(self, request, pk):
        entrenador_object = get_object_or_404(entrenador, pk=pk)
        return render(request, 'entrenadores/entrenador_confirm_delete.html', {'entrenador': entrenador_object})
    
    def post(self, request, pk):
        entrenador_object = get_object_or_404(entrenador, pk=pk)
        entrenador_object.delete()
        return redirect('entrenador_list')
    
    