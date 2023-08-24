from .models import jugador, entrenador, Equipo, Partido 
# no sea el mismo equipolocal
equipo = Equipo.objects.exclude(id=Partido.equipo_local.id)

