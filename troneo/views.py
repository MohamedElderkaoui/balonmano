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
class JugadorListView(View):
    def get(self, request):
        players = JsonResponse(list(jugador.objects.all().values()), safe=False)
        cntx = {'players': players}
        return render(request, 'jugador_list.html',cntx)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Jugadores'
        context['title2'] = 'Jugadores'
        c
        return context
    

class JugadorDetailView(View):
    def get(self, request, pk):
        player =JsonResponse(list(jugador.objects.filter(pk=pk).values()), safe=False)
        return render(request, 'jugador_detail.html', {'player': player})

class JugadorCreateView(View):
    def get(self, request):
        form = JugadorForm()
        return render(request, 'jugador_form.html', {'form': form})
    
    def post(self, request):
        form = JugadorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('jugador_list')
        return render(request, 'jugador_form.html', {'form': form})

class JugadorUpdateView(View):
    def get(self, request, pk):
        player = get_object_or_404(jugador, pk=pk)
        form = JugadorForm(instance=player)
        return render(request, 'jugador_form.html', {'form': form})
    
    def post(self, request, pk):
        player = get_object_or_404(jugador, pk=pk)
        form = JugadorForm(request.POST, request.FILES, instance=player)
        if form.is_valid():
            form.save()
            return redirect('jugador_list')
        return render(request, 'jugador_form.html', {'form': form})

class JugadorDeleteView(View):
    def get(self, request, pk):
        player = get_object_or_404(jugador, pk=pk)
        return render(request, 'jugador_confirm_delete.html', {'player': player})
    
    def post(self, request, pk):
        player = get_object_or_404(jugador, pk=pk)
        player.delete()
        return redirect('jugador_list')
    
class EntrenadorListView(View):
    def get(self, request):
        coachs = entrenador.objects.all()
        return render(request, 'entrenador_list.html', {'coachs': coachs})

class EntrenadorDetailView(View):
    def get(self, request, pk):
        coach = get_object_or_404(entrenador, pk=pk)
        return render(request, 'entrenador_detail.html', {'coach': coach})
    
class EntrenadorCreateView(View):
    def get(self, request):
        form = EntrenadorForm()
        return render(request, 'entrenador_form.html', {'form': form})
    
    def post(self, request):
        form = EntrenadorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('entrenador_list')
        return render(request, 'entrenador_form.html', {'form': form})

class EntrenadorUpdateView(View):
    def get(self, request, pk):
        coach = get_object_or_404(entrenador, pk=pk)
        form = EntrenadorForm(instance=coach)
        return render(request, 'entrenador_form.html', {'form': form})
    
    def post(self, request, pk):
        coach = get_object_or_404(entrenador, pk=pk)
        form = EntrenadorForm(request.POST, request.FILES, instance=coach)
        if form.is_valid():
            form.save()
            return redirect('entrenador_list')
        return render(request, 'entrenador_form.html', {'form': form})

class EntrenadorDeleteView(View):
    def get(self, request, pk):
        coach = get_object_or_404(entrenador, pk=pk)
        return render(request, 'entrenador_confirm_delete.html', {'coach': coach})
    
    def post(self, request, pk):
        coach = get_object_or_404(entrenador, pk=pk)
        coach.delete()
        return redirect('entrenador_list')
    
class EquipoListView(View):
    def get(self, request):
        teams = Equipo.objects.all()
        return render(request, 'equipo_list.html', {'teams': teams})

class EquipoDetailView(View):
    def get(self, request, pk):
        team = get_object_or_404(Equipo, pk=pk)
        return render(request, 'equipo_detail.html', {'team': team})

class EquipoCreateView(View):
    def get(self, request):
        form = EquipoForm()
        return render(request, 'equipo_form.html', {'form': form})
    
    def post(self, request):
        form = EquipoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('equipo_list')
        return render(request, 'equipo_form.html', {'form': form})
    
class EquipoUpdateView(View):
    def get(self, request, pk):
        team = get_object_or_404(Equipo, pk=pk)
        form = EquipoForm(instance=team)
        return render(request, 'equipo_form.html', {'form': form})
    
    def post(self, request, pk):
        team = get_object_or_404(Equipo, pk=pk)
        form = EquipoForm(request.POST, request.FILES, instance=team)
        if form.is_valid():
            form.save()
            return redirect('equipo_list')
        return render(request, 'equipo_form.html', {'form': form})

class EquipoDeleteView(View):
    def get(self, request, pk):
        team = get_object_or_404(Equipo, pk=pk)
        return render(request, 'equipo_confirm_delete.html', {'team': team})
    
    def post(self, request, pk):
        team = get_object_or_404(Equipo, pk=pk)
        team.delete()
        return redirect('equipo_list')
    
class PartidoListView(View):
    def get(self, request):
        matches = Partido.objects.all()
        return render(request, 'partido_list.html', {'matches': matches})
    
class PartidoDetailView(View):
    def get(self, request, pk):
        match = get_object_or_404(Partido, pk=pk)
        return render(request, 'partido_detail.html', {'match': match})
    
class PartidoCreateView(View):
    def get(self, request):
        form = PartidoForm()
        return render(request, 'partido_form.html', {'form': form})
    
    def post(self, request):
        form = PartidoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # relacion_entre_entrenadores_y_equipos
            
            quipo_local = form.cleaned_data['equipo_local']
            equipo_visitante = form.cleaned_data['equipo_visitante']
            
            relacion_entre_equipos_y_partidos.objects.create(equipo=quipo_local, partido=form.instance)
            relacion_entre_equipos_y_partidos.objects.create(equipo=equipo_visitante, partido=form.instance)
            
            return redirect('partido_list')
        return render(request, 'partido_form.html', {'form': form})

class PartidoUpdateView(View):
    def get(self, request, pk):
        match = get_object_or_404(Partido, pk=pk)
        form = PartidoForm(instance=match)
        return render(request, 'partido_form.html', {'form': form})
    
    def post(self, request, pk):
        match = get_object_or_404(Partido, pk=pk)
        form = PartidoForm(request.POST, request.FILES, instance=match)
        if form.is_valid():
            form.save()
            match.equipo_local = form.cleaned_data['equipo_local']
            match.equipo_visitante = form.cleaned_data['equipo_visitante']
            relacion_entre_equipos_y_partidos.objects.filter(partido=match).delete()
            relacion_entre_equipos_y_partidos.objects.create(equipo=match.equipo_local, partido=match)
            relacion_entre_equipos_y_partidos.objects.create(equipo=match.equipo_visitante, partido=match)
            return redirect('partido_list')
        return render(request, 'partido_form.html', {'form': form})
    
class PartidoDeleteView(View):
    def get(self, request, pk):
        match = get_object_or_404(Partido, pk=pk)
        return render(request, 'partido_confirm_delete.html', {'match': match})
    
    def post(self, request, pk):
        match = get_object_or_404(Partido, pk=pk)
        match.delete()
        return redirect('partido_list')
    
class ClasificacionListView(View):
    def get(self, request):
        clasificaciones = clasificacion.objects.all()
        return render(request, 'clasificacion_list.html', {'clasificaciones': clasificaciones})
    
class ClasificacionDetailView(View):
    def get(self, request, pk):
        clasificacione = get_object_or_404(clasificacion, pk=pk)
        for partido  in Partido.objects.all():
            if partido.equipo_local == clasificacione.equipo:
                clasificacione.partidos_jugados += 1
                clasificacione.goles_favor += partido.goles_local
                clasificacione.goles_contra += partido.goles_visitante
                if partido.goles_local > partido.goles_visitante:
                    clasificacione.partidos_ganados += 1
                    clasificacione.puntos += 3
                elif partido.goles_local < partido.goles_visitante:
                    clasificacione.partidos_perdidos += 1
                else:
                    clasificacione.partidos_empatados += 1
                    clasificacione.puntos += 1
            elif partido.equipo_visitante == clasificacione.equipo:
                clasificacione.partidos_jugados += 1
                clasificacione.goles_favor += partido.goles_visitante
                clasificacione.goles_contra += partido.goles_local
                if partido.goles_local < partido.goles_visitante:
                    clasificacione.partidos_ganados += 1
                    clasificacione.puntos += 3
                elif partido.goles_local > partido.goles_visitante:
                    clasificacione.partidos_perdidos += 1
                else:
                    clasificacione.partidos_empatados += 1
                    clasificacione.puntos += 1
        return render(request, 'clasificacion_detail.html', {'clasificacione': clasificacione})

