from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import jugador, entrenador, Equipo, Partido, clasificacion, relacion_entre_jugadores_y_equipos, relacion_entre_entrenadores_y_equipos, relacion_entre_equipos_y_partidos

@admin.register(jugador)
class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'edad', 'posicion', 'nacionalidad')
    search_fields = ('nombre', 'apellido', 'nacionalidad')

@admin.register(entrenador)
class EntrenadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'edad', 'nacionalidad')
    search_fields = ('nombre', 'apellido', 'nacionalidad')


@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad', 'entrenador')
    search_fields = ('nombre', 'ciudad', 'entrenador__nombre', 'entrenador__apellido')
    
    

@admin.register(Partido)
class PartidoAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'equipo_local', 'equipo_visitante', 'goles_local', 'goles_visitante')
    list_filter = ('equipo_local', 'equipo_visitante')
    date_hierarchy = 'fecha'

@admin.register(clasificacion)
class ClasificacionAdmin(admin.ModelAdmin):
    list_display = ('equipo', 'puntos', 'partidos_jugados', 'partidos_ganados', 'partidos_empatados', 'partidos_perdidos', 'goles_favor', 'goles_contra')
    list_filter = ('equipo',)
    
@admin.register(relacion_entre_jugadores_y_equipos)
class JugadoresEquiposAdmin(admin.ModelAdmin):
    list_display = ('jugador', 'equipo')
    list_filter = ('jugador', 'equipo')
    
@admin.register(relacion_entre_entrenadores_y_equipos)
class EntrenadoresEquiposAdmin(admin.ModelAdmin):
    list_display = ('entrenador', 'equipo')
    list_filter = ('entrenador', 'equipo')

@admin.register(relacion_entre_equipos_y_partidos)
class EquiposPartidosAdmin(admin.ModelAdmin):
    list_display = ('equipo', 'partido')
    list_filter = ('equipo', 'partido')
